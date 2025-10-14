from django.contrib import admin
from.models import Waiter,Category,Customer_order,Food_item,Menu,Menu_item,Order_item,Restaurant_table
# Register your models here.
class WaiterAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","contact","gender")
admin.site.register(Waiter,WaiterAdmin)

class CustomerOrderAdmin (admin.ModelAdmin):
    list_display = ("table_no","waiterid","order_status","order_date")
admin.site.register(Customer_order,CustomerOrderAdmin)

class Food_itemAdmin(admin.ModelAdmin):
    list_display = ("name","category_id")
admin.site.register(Food_item,Food_itemAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
admin.site.register(Category,CategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("id","menu_name","price")
admin.site.register(Menu,MenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id","qauntity","menu_id")
admin.site.register(Menu_item,MenuItemAdmin)

class OrderitemAdmin(admin.ModelAdmin):
    list_display = ("id","menu_id","customer_order_id","Quantity")
admin.site.register(Order_item,OrderitemAdmin)

class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = ("id","table_no","status","location")
admin.site.register(Restaurant_table,RestaurantTableAdmin)

    
    