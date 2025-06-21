
from django.contrib import admin
from .models import Employee, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    search_fields = ('name', 'email', 'department__name')
    list_filter = ('department',)

