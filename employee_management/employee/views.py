from django.shortcuts import render, redirect

# Create your views here.

from .models import Employee



def employee_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by')
    
    if search_query:
        employees = Employee.objects.filter(name__icontains=search_query) | Employee.objects.filter(position__icontains=search_query)
    else:
        employees = Employee.objects.all()
    
    if sort_by == 'name':
        employees = employees.order_by('name')
    elif sort_by == 'age':
        employees = employees.order_by('age')
    elif sort_by == 'position':
        employees = employees.order_by('position')
    elif sort_by == 'salary':
        employees = employees.order_by('salary')
    
    return render(request, 'employee_list.html', {'employees': employees, 'search': search_query, 'sort_by': sort_by})


def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        position = request.POST['position']
        salary = int(request.POST['salary'])
        Employee.objects.create(name=name, age=age, position=position, salary=salary)
        return redirect('employee_list')
    return render(request, 'add_employee.html')

def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.age = int(request.POST['age'])
        employee.position = request.POST['position']
        employee.salary = int(request.POST['salary'])
        employee.save()
        return redirect('employee_list')
    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'delete_employee.html', {'employee': employee})

def search_employee(request):
    query = request.GET.get('q')
    employees = Employee.objects.filter(name__icontains=query) | Employee.objects.filter(position__icontains=query)
    return render(request, 'search_employee.html', {'employees': employees})

def sort_employee_list(request, sort_by):
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        employees = Employee.objects.order_by('name')
    elif sort_by == 'age':
        employees = Employee.objects.order_by('age')
    elif sort_by == 'position':
        employees = Employee.objects.order_by('position')
    elif sort_by == 'salary':
        employees = Employee.objects.order_by('salary')
    else:
        employees = Employee.objects.all()
    return render(request, 'sort_employee_list.html', {'employees': employees})
