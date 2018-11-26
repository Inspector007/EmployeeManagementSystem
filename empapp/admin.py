from django.contrib import admin

# Register your models here.

from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('empName','empEmail','empPan')
	list_filter = ('empName','empEmail','empPan')
	search_fields = ('empName','empEmail','empPan')
	ordering = ['empName','empEmail']
admin.site.register(Employee,EmployeeAdmin)

