from django.forms import ModelForm
from Restaurantapp.models import Waiter, Category 

class WaiterForm (ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'

class CategoryForm (ModelForm):
    class Meta:
        model = Category
        fields = '__all__'