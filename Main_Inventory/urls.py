from django.contrib import admin
from django.urls import path

from Main_Inventory import views

urlpatterns = [
    path('',views.load_login,name="login"),
    path('login',views.load_login,name="login"),
    path('logout',views.load_logout,name="logout"),
    path('home',views.load_home,name="home"),
    path('registration',views.load_registration,name="registration"),
    path('add_existing',views.load_add_existing,name="add_existing"),
    path('add_pro/<pro_id>/',views.add_product,name="add_pro"),
    path('add_new_product',views.add_new_product,name="add_new_product"),
    path('load_sell_item',views.load_sell_item,name="load_sell_item"),
    path('add_to_cart/<pro_id>/',views.add_to_cart,name="add_to_cart"),
    path('delete_from_cart/<cart_id>/',views.delete_from_cart,name="delete_from_cart"),
    path('sell_item',views.sell_item,name="sell_item"),
    path('history/<bill_id>/',views.history,name="history"),
    path('get_chartdata',views.get_chartdata,name="get_chartdata"),
    path('get_userdata',views.get_userdata,name="get_userdata"),
    path('get_stockdata',views.get_stockdata,name="get_stockdata")

]
