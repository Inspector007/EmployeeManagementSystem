# Create your views here.

from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.http import HttpResponse

from . forms import EmployeeForm
from .models import Employee



def home(request):
    return render(request,'base.html')

def employeeadd(request):
    msg = ''
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            e = Employee()
            cd = form.cleaned_data
            e.empName = request.POST.get('empName')
            e.empEmail = request.POST.get('empEmail')
            e.empPan = request.POST.get('empPan')
            e.save()
            msg = '{0} Employee Saved'.format(e.empName)
            form = EmployeeForm()
            # return render(request, 'empapp/employee_add.html',{'form': form})
    else:
        form = EmployeeForm()
    return render(request, 'empapp/employee_add.html', {'form': form,'msg':msg})
    # return HttpResponse("It works Successfully !!")


class EmployeeListView(ListView):
    queryset = Employee.objects.all()
    context_object_name = 'employees'
    paginate_by = 3
    template_name = 'empapp/employee_list.html'


def employeelist(request):
    object_list = Employee.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    return render(request,'empapp/employee_list.html',{'page':page, 'employees':employees})

def employeedetail(request,name,pan):
    employee = get_object_or_404(Employee, empName = name, empPan = pan)
    return render(request,'empapp/employee_detail.html',{'employee':employee})

def employeeedit(request):
    employee = request.employee
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            e = Employee()
            cd = form.cleaned_data
            e.empName = request.POST.get('empName')
            e.empEmail = request.POST.get('empEmail')
            e.empPan = request.POST.get('empPan')
            e.save()
            msg = '{0} Employee Saved'.format(e.empName)
            form = EmployeeForm()
            # return render(request, 'empapp/employee_add.html',{'form': form})
    else:
        form = EmployeeForm(instance=)
    return render(request, 'empapp/employee_add.html', {'form': form,'msg':msg})
    

