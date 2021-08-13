from django.shortcuts import render

# Create your views here.
#8000/crm/employee/add
def employee_add(request):
    return render(request,"employee_add.html")

def employee_preview(request,id):
    return render(request,"employee_preview.html")

def employee_edit(request,id):
    return render(request,"employee_edit.html")

def employee_remove(request,id):
    return render(request,"employee_remove.html")