from django.contrib import admin

# Register your models here.
from hotel.models import *

@admin.register(branch)
class branchAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'location', 'phone']

@admin.register(staff)
class staffAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'category', 'gender', 'branchName']
    
@admin.register(clients)
class clientsAdmin(admin.ModelAdmin):
    list_display = ['name','address', 'phone', 'identity', 'gender', 'BranchName', 'order', 'bill', 'roomNo']

@admin.register(food)
class foodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

@admin.register(orders)
class orderAdmin(admin.ModelAdmin):
    list_display = ['name', 'items']
