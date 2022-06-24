from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
TYPE = [
('MX', 'Mixed'),
('MT', 'Meaty'),
('VG', 'Vegeterian'),
('ST', 'Starchy'),
]

class Menu(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=600)
    type = models.CharField(max_length=2, choices=TYPE)
    country_of_origin = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Menu'
    
    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Partners'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    allergins = models.CharField(max_length=200)
    unit_serving = models.IntegerField()
    menu = models.ManyToManyField(Menu)
    partner = models.ManyToManyField(Partner)

    class Meta:
        verbose_name_plural = 'Menu Items'
    
    def __str__(self):
        return self.menu

class Supplier(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=200)  

    class Meta:
        verbose_name_plural = 'Clients'
    
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200) 
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True) 
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=30)
    unit_price = models.IntegerField()
    profit_per_serving = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Ingredients'
    
    def __str__(self):
        return self.name


EMPLOYMENT_STATUS = [
('FT', 'Full-Time'),
('PT', 'Part-Time'),
]

GENDER = [
('ML', 'Male'),
('FM', 'Female'),
('GN', 'Prefer not to say'),
]

DEPARTMENT = [
('Mn', 'Management'),
('TP', 'Transportion'),
('LG', 'Logistics/Operations'),
('MK', 'Marketing'),
('SV', 'Customer Service'),
('FN', 'Finance'),
]

ROLE = [
('MG', 'Manager'),
('JM', 'Junior Manager'),
('OS', 'Ordinary staff'),
('DR', 'Director'),
]

class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    department = models.CharField(max_length=2, choices=DEPARTMENT, null=True)
    phone = models.CharField(max_length=13)
    national_registration_number = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)
    employment_status = models.CharField(max_length=2, choices=EMPLOYMENT_STATUS)
    role = models.CharField(max_length=2, choices=ROLE, null=True)
    

    class Meta:
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return self.full_name


INVENTORY_TYPE = [
('EQ', 'Equipment'),
('MT', 'Material'),
('PS', 'Perishables'),
]

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=INVENTORY_TYPE)
    unit = models.CharField(max_length=30)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True) 
    date_proccured = models.DateField()

    class Meta:
        verbose_name_plural = 'Inventory'
    
    def __str__(self):
        return self.name
    
EVENT_TYPE = [
('AN', 'Anniversary'),
('WD', 'Wedding'),
('FN', 'Funeral'),
('BD', 'Birthday'),
('CO', 'Coporate'),
('GT', 'Get-together'),
]

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_type = models.CharField(max_length=2, choices=EVENT_TYPE)
    contract_sum = models.IntegerField()
    budget = models.IntegerField()
    actual = models.IntegerField()
    ordinary_guests = models.IntegerField()
    vip_guests = models.IntegerField()
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True) 
    department = models.CharField(max_length=2, choices=DEPARTMENT, null=True)

    class Meta:
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return self.name

EXPENSE_TYPE = [
('EO', 'Extra Over'),
('AC', 'Accomodation'),
('CA', 'Communication/Airtime'),
('KT', 'Kitchen'),
('ME', 'Materials and Equipment'),
('FI', 'Food Items'),
('DM', 'Damages'),
('VM', 'Vehicle repair and Maintenance'),
('GS', 'Gas'),
('UN', 'Uniform')
]

ORDER_STATUS = [
('PC', 'Purchased'),
('RT', 'Rented')
]

PAYMENT_METHOD = [
('CS', 'Cash'),
('CR', 'Card'),
('CD', 'Credit'),
('AM', 'Airtel Money'),
('MM', 'MTN Money'),
('OT', 'Other')
]


class Expenses(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=2, choices=DEPARTMENT, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    expense_type = models.CharField(max_length=2, choices=EXPENSE_TYPE)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=2, choices=ORDER_STATUS)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD)
    

    class Meta:
        verbose_name_plural = 'Expenses'
    
    def __str__(self):
        return self.date


PEFORMANCE_RANKING = [
('EX', 'Excellent'),
('GD', 'Good'),
('AV', 'Average'),
('CI', 'Below Average')

]
class Peformance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True) 
    department = models.CharField(max_length=2, choices=DEPARTMENT, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField()
    peformance = models.CharField(max_length=2, choices=PEFORMANCE_RANKING)
    date = models.DateField()
    

    class Meta:
        verbose_name_plural = 'Staff Peformance'
    
    def __str__(self):
        return self.employee