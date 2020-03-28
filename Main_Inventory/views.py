from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User ,auth
from django.shortcuts import render, redirect
from django.db.models import IntegerField
from django.db.models.functions import Cast
from Main_Inventory.models import cart, bill, sold_products
from Main_Inventory.models import dataholder,bill_dataholder,main_bill_dataholder
import datetime

# Create your views here.
from Main_Inventory.models import emp_det, product


def load_logout(request):
    auth.logout(request)
    return render(request,'login.html')

def load_add_existing(request):
    pros = product.objects.all()

    return render(request,'add_existing.html',{'proli':pros})


def add_product(request,pro_id):
    str="quan_"+pro_id
    qua=request.POST[str]

    obj=product.objects.get(id=pro_id)
    obj.quantity+=int(qua)
    obj.save()

    pros = product.objects.all()
    return render(request,'add_existing.html',{'proli':pros})

def add_new_product(request):
    
    name=request.POST['name']
    cost = request.POST['cost']
    quantity = request.POST['quantity']
    name=name.lower()
    obj=product()
    obj.name=name
    obj.cost=cost
    obj.quantity=quantity
    origname=name.title()
    if product.objects.filter(name=name).exists():
        messages.info(request,origname+' is Already Present TRY AGAIN!!!')
    else:
        product.objects.create(name=name,quantity=quantity,cost=cost)

    pros = product.objects.all()
    return render(request, 'add_existing.html', {'proli': pros})

def load_home(request):

    pros=product.objects.all()

    return render(request,'Home.html',{'proli':pros})


def load_registration(request):


    if request.method=='POST':
        name = request.POST['nameabc']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        gender = request.POST['Gender']
        dob = request.POST['dob']
        flag=0
        if User.objects.filter(username=username).exists():
            messages.info(request,'USERNAME ALREADY PRESENT')
            flag=1
        if User.objects.filter(email=email).exists():
            flag=1
            messages.info(request, 'EMAIL ALREADY PRESENT')
        if emp_det.objects.filter(mobile=mobile).exists():
            flag=1
            messages.info(request, 'MOBILE ALREADY PRESENT')
        if flag==0:
            User.objects.create_user(username=username,email=email,password=password)
            emp_det.objects.create(name=name,username=username,mobile=mobile,address=address,email=email,gender=gender,dob=dob)
            return render(request, 'Login.html')
        else:
            messages.info(request, '!!! PLEASE TRY AGAIN !!!')
            return render(request, 'Registration.html')

    return render(request,'Registration.html')


def load_login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        ispresent=auth.authenticate(username=username,password=password)
        if ispresent is not None:
            auth.login(request, ispresent)
            return redirect("home")
        else:
            messages.info(request,'Invalid credentials TRY AGAIN!!!')
            return render(request, 'Login.html')


    return render(request,'Login.html')


def add_to_cart(request,pro_id):
    user = request.user.username
    quantity=request.POST['quan_'+pro_id]
    selling=request.POST['sp_'+pro_id]

    if cart.objects.filter(empusername=user).filter(productid=pro_id).filter(sellingprice=selling).exists():

        tempobj=cart.objects.get(productid=pro_id,sellingprice=selling,empusername=user)
        tempobj.quantity+=int(quantity)
        tempobj.save()
    else:
        cart.objects.create(empusername=user,quantity=quantity,sellingprice=selling,productid=pro_id)

    obj = product.objects.get(id=pro_id)
    obj.quantity -= int(quantity)
    obj.save()

    return redirect('load_sell_item')



def load_sell_item(request):

    pros = product.objects.all()
    user = request.user.username
    cartobj = cart.objects.filter(empusername=user)
    profit=0
    total=0
    passinglist=[]
    for item in cartobj:
        obj = product.objects.get(id=item.productid)
        passingobj = dataholder()
        passingobj.cart_id=item.id
        passingobj.pro_id=item.productid
        passingobj.sellingprice=item.sellingprice
        passingobj.quantity=item.quantity
        passingobj.name = obj.name
        passingobj.cost = obj.cost
        profit +=(passingobj.sellingprice-passingobj.cost)*passingobj.quantity
        passinglist.append(passingobj)
        total+=passingobj.sellingprice*passingobj.quantity
    return render(request,'sell_item.html',{'proli':pros,'pass':passinglist,'profit':profit,'total':total})

def delete_from_cart(request,cart_id):
    user = request.user.username
    print("delete frommm cart")
    quantity=request.POST['quan_'+cart_id]
    product_id=request.POST['pro_'+cart_id]


    obj=cart.objects.get(id=cart_id)
    obj.delete()

    objpro = product.objects.get(id=product_id)
    objpro.quantity += int(quantity)
    objpro.save()

    return redirect('load_sell_item')



def sell_item(request):
    user = request.user.username
    carto = cart.objects.filter(empusername=user)

    now=datetime.datetime.now()
    profit=request.POST['profit']
    customer = request.POST['cust']
    print("{}-{}-{}-{}-{}-{}-{}".format(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond))

    datetimestr=datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)
    bill.objects.create(empusername=user,date=datetimestr,profit=profit,soldto=customer)

    obj=bill.objects.get(date=datetimestr)

    print(obj.id)
    cartobj = cart.objects.filter(empusername=user)

    for item in cartobj:
        pro_id=item.productid
        quantity=item.quantity
        sellingprice=item.sellingprice
        billid=obj.id
        sold_products.objects.create(productid=pro_id,quantity=quantity,sellingprice=sellingprice,billid=billid)
        item.delete()

    return redirect('load_sell_item')


def history(request,bill_id):
    user=request.user.username
    tempbillobj=bill.objects.filter(empusername=user)
    billobj=list()
    for abc in tempbillobj:
        testobj=main_bill_dataholder()
        testobj.billid=str(abc.id)
        testobj.soldto=abc.soldto
        testobj.profit=abc.profit
        testobj.date=abc.date
        billobj.append(testobj)

    billdet=list()
    if bill_id!='none':
        soldobj=sold_products.objects.filter(billid=bill_id)
        for sold in soldobj:
            proname=product.objects.get(id=sold.productid)
            billdetobj=bill_dataholder()
            billdetobj.name=proname.name
            billdetobj.quantity=sold.quantity
            billdetobj.sellingprice=sold.sellingprice
            billdet.append(billdetobj)
    billidabc=str(bill_id)
    return render(request,'history.html',{'bills':billobj,'billdet':billdet,'bill_idabc':billidabc})


def get_chartdata(request):

    obj=bill.objects.all()
    labels=list()
    datalist = list()
    for item in obj:
        date=str(item.date)
        dt1=date.split()
        finaldate=dt1[0]
        profit=item.profit
        labels.append(finaldate)
        datalist.append(profit)

    data={
        "response_labels":labels,
        "response_data":datalist
    }
    return JsonResponse(data)
def get_userdata(request):

    obj=bill.objects.filter(empusername=request.user.username)
    labels=list()
    datalist = list()
    for item in obj:
        date=str(item.date)
        dt1=date.split()
        finaldate=dt1[0]
        profit=item.profit
        labels.append(finaldate)
        datalist.append(profit)

    data={
        "response_labels":labels,
        "response_data":datalist
    }
    return JsonResponse(data)
def get_stockdata(request):

    obj=product.objects.all()
    labels=list()
    datalist = list()
    for item in obj:
        name=item.name
        quantity=item.quantity
        labels.append(name)
        datalist.append(quantity)

    data={
        "response_labels":labels,
        "response_data":datalist
    }
    return JsonResponse(data)