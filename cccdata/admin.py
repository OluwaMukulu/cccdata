from django.contrib import admin
from .models import Menu,Partner,Item, Supplier,Client,Ingredients,Employee,Inventory,Event,Activity,Expenses,Peformance


admin.site.site_header = 'Classic Cuisine Caterers'
admin.site.site_title = 'GRiL Technology'
admin.site.index_title = 'Management Information System'
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'gender', 'address', 'department', 'employment_status', 'role')
    search_fields = ['full_name', 'national_registration_number']
    list_filter = ('employment_status', 'role')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'country_of_origin')
    search_fields = ['name']
    list_filter = ('type', 'country_of_origin')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    search_fields = ['name']

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu','unit_serving')
    search_fields = ['name']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    search_fields = ['name']

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    search_fields = ['name']

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name','item', 'supplier', 'unit_price','quantity', 'profit_per_serving')
    search_fields = ['name']

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'supplier', 'unit_price', 'quantity', 'date_proccured')
    search_fields = ['name']

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'event_type','start_date', 'end_date', 'contract_sum', 'ordinary_guests','vip_guests', 'city')
    search_fields = ['name']
    list_filter = ('country')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'event','supervisor', 'status')
    search_fields = ['name']
    list_filter = ('status', 'supervisor')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'expense_type','activity','event','date', 'unit_price', 'quantity')
    search_fields = ['name']
    list_filter = ('expense_type')


class PeformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'event', 'salary', 'peformance','date')
    search_fields = ['employee']
    list_filter = ('department', 'peformance','event')

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