from django.forms import ModelForm
from Restaurantapp.models import Waiter

class WaiterForm (ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'