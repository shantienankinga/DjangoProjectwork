from django.db import models
GENDER_OPTIONS =[
    ("M","Male"),
    ("F","Female"),
]
# Create your models here.
class Waiter(models.Model):
    first_name = models.CharField(max_length=30,verbose_name="waiter_name")
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_OPTIONS)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="category_name")
    def __str__(self):
        return self.name
class Menu (models.Model):
    menu_name = models.CharField(max_length=30)
    price = models.IntegerField()
    def __str__(self):
        return self.menu_name
    
class Restaurant_table(models.Model):
    table_no= models.CharField(max_length=20)
    status = models.CharField (max_length=10)
    location = models.CharField(max_length=15) 
    def __str__(self):
        return self.status
    
class Menu_item (models.Model):
    qauntity = models.IntegerField()
    menu_id = models.ForeignKey(Menu , verbose_name=("menuid") , on_delete= models.CASCADE)
    
class Food_item(models.Model):
    name = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category, verbose_name="categoryid" , on_delete= models.CASCADE)
    def __str__(self):
        return self.name
    
class Customer_order (models.Model):
    table_no = models.CharField(max_length=20) 
    waiterid = models.ForeignKey(Waiter, verbose_name="_waiter_id" , on_delete= models.CASCADE)
    order_status = models.CharField(max_length=30) 
    order_date = models .DateField(auto_now=False)
    def __str__(self):
        return self.order_status
    
class Order_item (models.Model) : 
    menu_id = models.ForeignKey(Menu, verbose_name="menuid" , on_delete= models.CASCADE)
    customer_order_id = models.ForeignKey(Customer_order, verbose_name="customer_order_id" , on_delete= models.CASCADE)
    Quantity =models.IntegerField() 

    
    
