from django.shortcuts import render
from Restaurantapp.forms import WaiterForm
from Restaurantapp.models import Waiter
from django.shortcuts import render, redirect
# Create your views here.
def category_veiw(request):
    return render (request, 'category.html')
def Customer_order_veiw(request):
    return render (request, 'Customer_order.html')
def firsthome_veiw(request):
    return render (request, 'firsthome.html')
def fooditem_veiw(request):
    return render(request,'fooditem.html')
def login_veiw(request):
    return render (request,'login.html')
def menu_veiw(request):
    return render (request,'menu.html')
def menuitem_veiw(request):
    return render (request,'menuitem.html')
def Order_item_veiw(request):
    return render (request,'Order_item.html')
def restaurant_table_veiw(request):
    return render (request,'restaurant_table.html')
def waiter_veiw(request):
    return render (request,'waiter.html')

def add_waiter_veiw (request):
    message = ''
    if request.method =="POST":
        waiter_form = WaiterForm(request.POST)
        if waiter_form.is_valid():
            waiter_form.save()
            message="waiter added successfully"
    else:
        waiter_form = WaiterForm()
        waiters = Waiter.objects.all()
    context = {
        'form' : waiter_form,
        'msg' : message,
        'waiters' : waiters,
    }
    return render(request ,"add_waiter.html" , context)

def edit_waiter_veiw(request, waiter_id):
    message=''
    waiter = Waiter.objects.get(id = waiter_id)
    if request.method == "POST":
        Waiter_form  = WaiterForm(request.POST, instance=waiter)
        if Waiter_form.is_valid():
            Waiter_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        Waiter_form = WaiterForm(instance=waiter)
    context ={
        'form' : Waiter_form,
        'waiter' : waiter,
        'message' : message,
    }
    return render (request ,'edit_waiter.html',context)

def delete_waiter_veiw(request, waiter_id) :
    waiter = Waiter.objects.get(id=waiter_id)
    waiter.delete()
    return redirect (add_waiter_veiw)