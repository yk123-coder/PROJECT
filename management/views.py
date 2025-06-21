
from django.shortcuts import render
from .models import Employee
# from .models import Department
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'management/employee_list.html', {'employees': employees})

