from django.contrib import admin
from .models import Menu,Partner,Item, Supplier,Client,Ingredients,Employee,Inventory,Event,Activity,Expenses,Peformance



admin.site.site_header = 'Classic Cuisine Caterers'
admin.site.site_title = 'GRiL Technology'
admin.site.index_title = 'Management Information System'
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'gender', 'address', 'department', 'employment_status', 'role')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'country_of_origin')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_serving')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name','item', 'supplier', 'unit_price', 'profit_per_serving')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'supplier', 'unit_price', 'quantity', 'date_proccured')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'event_type','start_date', 'end_date', 'contract_sum', 'ordinary_guests','vip_guests', 'city')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'event','start_date', 'end_date')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'expense_type', 'unit_price', 'quantity', 'order_status','payment_method','event','date')

class PeformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'event', 'salary', 'peformance','date')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Expenses, ExpenseAdmin)
admin.site.register(Peformance, PeformanceAdmin)