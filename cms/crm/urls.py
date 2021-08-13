from django.urls import path
from crm import views
urlpatterns=[
    path("employee/add",views.employee_add),
    path("employee/preview/<int:id>",views.employee_preview),
    path("employee/edit/<int:id>",views.employee_edit),
    path("employee/remove/<int:id>",views.employee_remove)
]
