"""
URL configuration for Restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Restaurantapp.views import category_veiw, Customer_order_veiw,firsthome_veiw,fooditem_veiw,login_veiw,menu_veiw,menuitem_veiw,Order_item_veiw,restaurant_table_veiw,waiter_veiw,add_waiter_veiw,edit_waiter_veiw,delete_waiter_veiw,add_category_veiw,edit_category_veiw
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',category_veiw, name='category_page'),
    path('Customer_order/' , Customer_order_veiw, name='customer_order_page'),
    path('firsthome_page/',firsthome_veiw, name='home_page'),
    path('fooditem_page/',fooditem_veiw,name='fooditem_page'),
    path('login/page',login_veiw,name='login_page'),
    path('menu/page',menu_veiw,name='menu_page'),
    path('menuitem/page',menuitem_veiw,name='menuitem_page'),
    path('Order_item/page',Order_item_veiw,name='order_item_page'),
    path('restaurant_table/page',restaurant_table_veiw,name='restaurant_table_page'),
    path('waiter/page',waiter_veiw,name='waiter_page'),
    path('add-waiter/page',add_waiter_veiw,name='add_waiter_page'),
    path('edit_waiter/<int:waiter_id>/',edit_waiter_veiw,name='edit_waiter_page'),
    path('delete_waiter/<int:waiter_id>/',delete_waiter_veiw,name='delete_waiter_page'),
    path('add_category/',add_category_veiw,name='add_category_page'),
    path('edit_category/<int:category_id/',edit_category_veiw,name='edit_category_page'),
]
