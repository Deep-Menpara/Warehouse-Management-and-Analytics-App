from django.db import models

# Create your models here.

class emp_det(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.TextField()
    username=models.TextField()
    mobile=models.TextField()
    address=models.TextField()
    email=models.TextField()
    gender=models.TextField()
    dob=models.TextField()


class product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name=models.TextField()
    cost = models.IntegerField()
    quantity = models.IntegerField()

class dataholder(models.Model):
    name=""
    cost=int()
    quantity=int()
    sellingprice=int()
    pro_id=int()
    cart_id=int()

class bill_dataholder(models.Model):
    name=""
    quantity=int()
    sellingprice=int()

class main_bill_dataholder(models.Model):
    billid=""
    soldto=""
    profit=int()
    date=""



class bill(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date=models.DateTimeField()
    empusername=models.TextField()
    soldto=models.TextField()
    profit=models.FloatField()

class cart(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    productid=models.TextField()
    sellingprice=models.IntegerField()
    quantity=models.IntegerField()
    empusername = models.TextField()

class sold_products(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    productid=models.TextField()
    billid = models.TextField()
    sellingprice =models.IntegerField()
    quantity =models.IntegerField()

