from django.forms import ModelForm
from Restaurantapp.models import Waiter, Category , Menu,Menu_item,Food_item,Order_item,Customer_order,Restaurant_table

class WaiterForm (ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'

class CategoryForm (ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class MenuForm (ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        
class MenuitemForm (ModelForm):
    class Meta:
        model = Menu_item
        fields = '__all__'
        
class FooditemForm (ModelForm):
    class Meta:
        model = Food_item
        fields = '__all__'

class OrderitemForm (ModelForm):
    class Meta:
        model = Order_item
        fields = '__all__'
        
class CustomerorderForm (ModelForm):
    class Meta:
        model = Customer_order
        fields = '__all__'
        
class RestuaranttableForm (ModelForm):
    class Meta:
        model = Restaurant_table
        fields = '__all__'
        