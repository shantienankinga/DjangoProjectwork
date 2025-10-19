from django.shortcuts import render
from Restaurantapp.forms import WaiterForm,CategoryForm , MenuForm,MenuitemForm,FooditemForm,OrderitemForm,CustomerorderForm,RestuaranttableForm
from Restaurantapp.models import Waiter,Category , Menu , Menu_item,Food_item,Order_item,Customer_order,Restaurant_table
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
    waiters = Waiter.objects.all()
    if request.method =="POST":
        waiter_form = WaiterForm(request.POST)
        if waiter_form.is_valid():
            waiter_form.save()
            message="waiter added successfully"
    else:
        waiter_form = WaiterForm()
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


def add_category_veiw(request):
    message = ''
    categorys = Category.objects.all()
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            message = "Category Added Successfully"
    else:
        category_form = CategoryForm()
        
    context = {
        'form' : category_form,
        'msg' : message,
        'categorys' : categorys,
    }
    return render(request ,"add_category.html", context)
def edit_category_veiw(request,category_id):
    message  = ''
    category = Category.objects.get(id = category_id)
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            message = "Changes Saved "
        else :
            message = "Form has invalid data"
    else:
        category_form = CategoryForm(instance=category)
        context = {
            'form' : category_form,
            'category' : category,
            'message' : message,

        }
        return render (request,'edit_category.html',context)
    
def delete_category_veiw(request, category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect (add_category_veiw)


def add_menu_veiw (request):
    message = ''
    menus = Menu.objects.all()
    if request.method =="POST":
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            message="menu added successfully"
    else:
        menu_form = MenuForm()
        
    context = {
        'form' : menu_form,
        'msg' : message,
        'menus' : menus,
    }
    return render(request ,"add_menu.html" , context)

def edit_menu_veiw(request, menu_id):
    message=''
    menu = Menu.objects.get(id = menu_id)
    if request.method == "POST":
        menu_form  = MenuForm(request.POST, instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        menu_form = MenuForm(instance=menu)
    context ={
        'form' : menu_form,
        'menu' : menu,
        'message' : message,
    }
    return render (request ,'edit_menu.html',context)

def delete_menu_veiw(request, menu_id) :
    menu = Menu.objects.get(id=menu_id)
    menu.delete()
    return redirect (add_menu_veiw)


def add_menu_item_veiw (request):
    message = ''
    menuitems = Menu_item.objects.all()
    if request.method =="POST":
        menu_item_form = MenuitemForm(request.POST)
        if menu_item_form.is_valid():
            menu_item_form.save()
            message="menuitem added successfully"
    else:
        menu_item_form = MenuitemForm()
        
    context = {
        'form' : menu_item_form,
        'msg' : message,
        'menuitems' : menuitems,
    }
    return render(request ,"add_menu_item.html" , context)

def edit_menu_item_veiw(request, menuitem_id):
    message=''
    menuitem = Menu_item.objects.get(id = menuitem_id)
    if request.method == "POST":
        menu_item_form  = MenuitemForm(request.POST, instance=menuitem)
        if menu_item_form.is_valid():
            menu_item_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        menu_item_form = MenuitemForm(instance=menuitem)
    context ={
        'form' : menu_item_form,
        'menuitem' : menuitem,
        'message' : message,
    }
    return render (request ,'edit_menu_item.html',context)

def delete_menu_item_veiw(request, menuitem_id) :
    menuitem = Menu_item.objects.get(id=menuitem_id)
    menuitem.delete()
    return redirect (add_menu_item_veiw)


def add_food_item_veiw (request):
    message = ''
    fooditems = Food_item.objects.all()
    if request.method =="POST":
        food_item_form = FooditemForm(request.POST)
        if food_item_form.is_valid():
            food_item_form.save()
            message="fooditem added successfully"
    else:
        food_item_form = FooditemForm()
        
    context = {
        'form' : food_item_form,
        'msg' : message,
        'fooditems' : fooditems,
    }
    return render(request ,"add_food_item.html" , context)

def edit_food_item_veiw(request, fooditem_id):
    message=''
    fooditem = Food_item.objects.get(id = fooditem_id)
    if request.method == "POST":
        food_item_form  = FooditemForm(request.POST, instance=fooditem)
        if food_item_form.is_valid():
            food_item_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        food_item_form = FooditemForm(instance=fooditem)
    context ={
        'form' : food_item_form,
        'fooditem' : fooditem,
        'message' : message,
    }
    return render (request ,'edit_food_item.html',context)

def delete_food_item_veiw(request, fooditem_id) :
    fooditem = Food_item.objects.get(id=fooditem_id)
    fooditem.delete()
    return redirect (add_food_item_veiw)



def add_order_item_veiw (request):
    message = ''
    orderitems = Order_item.objects.all()
    if request.method =="POST":
        order_item_form = OrderitemForm(request.POST)
        if order_item_form.is_valid():
            order_item_form.save()
            message="orderitem added successfully"
    else:
        order_item_form = OrderitemForm()
        
    context = {
        'form' : order_item_form,
        'msg' : message,
        'orderitems' : orderitems,
    }
    return render(request ,"add_order_item.html" , context)

def edit_order_item_veiw(request, orderitem_id):
    message=''
    orderitem = Order_item.objects.get(id = orderitem_id)
    if request.method == "POST":
        order_item_form  = OrderitemForm(request.POST, instance=orderitem)
        if order_item_form.is_valid():
            order_item_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        order_item_form = OrderitemForm(instance=orderitem)
    context ={
        'form' : order_item_form,
        'orderitem' : orderitem,
        'message' : message,
    }
    return render (request ,'edit_order_item.html',context)

def delete_order_item_veiw(request, orderitem_id) :
    orderitem = Order_item.objects.get(id=orderitem_id)
    orderitem.delete()
    return redirect (add_order_item_veiw)

def add_customer_order_veiw (request):
    message = ''
    customerorders = Customer_order.objects.all()
    if request.method =="POST":
        customer_order_form = CustomerorderForm(request.POST)
        if customer_order_form.is_valid():
            customer_order_form.save()
            message="customer-order added successfully"
    else:
        customer_order_form = CustomerorderForm()
        
    context = {
        'form' : customer_order_form,
        'msg' : message,
        'customerorders' : customerorders,
    }
    return render(request ,"add_customer_order.html" , context)

def edit_customer_order_veiw(request, customerorder_id):
    message=''
    customerorder = Customer_order.objects.get(id = customerorder_id)
    if request.method == "POST":
        customer_order_form  = CustomerorderForm(request.POST, instance=customerorder)
        if customer_order_form.is_valid():
            customer_order_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        customer_order_form = CustomerorderForm(instance=customerorder)
    context ={
        'form' : customer_order_form,
        'customerorder' : customerorder,
        'message' : message,
    }
    return render (request ,'edit_customer_order.html',context)

def delete_customer_order_veiw(request, customerorder_id) :
    customerorder = Customer_order.objects.get(id=customerorder_id)
    customerorder.delete()
    return redirect (add_customer_order_veiw)
    

def add_restuarant_table_veiw (request):
    message = ''
    restuaranttables = Restaurant_table.objects.all()
    if request.method =="POST":
        restuarant_table_form = RestuaranttableForm(request.POST)
        if restuarant_table_form.is_valid():
            restuarant_table_form.save()
            message="restuarant-table added successfully"
    else:
        restuarant_table_form = RestuaranttableForm()
        
    context = {
        'form' : restuarant_table_form,
        'msg' : message,
        'restuaranttables' : restuaranttables,
    }
    return render(request ,"add_restuarant_table.html" , context)

def edit_restuarant_table_veiw(request, restuaranttable_id):
    message=''
    restuaranttable = Restaurant_table.objects.get(id = restuaranttable_id)
    if request.method == "POST":
        restuarant_table_form  = RestuaranttableForm(request.POST, instance=restuaranttable)
        if restuarant_table_form.is_valid():
            restuarant_table_form.save()
            message="Changes saved sucessfully"
        else:
            message="form has invalid data"
    else:
        restuarant_table_form = RestuaranttableForm(instance=restuaranttable)
    context ={
        'form' : restuarant_table_form,
        'restuaranttable' : restuaranttable,
        'message' : message,
    }
    return render (request ,'edit_restuarant_table.html',context)

def delete_restuarant_table_veiw(request, restuaranttable_id) :
    restuaranttable = Restaurant_table.objects.get(id=restuaranttable_id)
    restuaranttable.delete()
    return redirect (add_restuarant_table_veiw)
