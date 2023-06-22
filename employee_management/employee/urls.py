from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('search/', views.search_employee, name='search_employee'),
    #path('sort/', views.sort_employee_list, name='sort_employee_list'),
    path('sort/<str:sort_by>/', views.sort_employee_list, name='sort_employee_list'),
]
