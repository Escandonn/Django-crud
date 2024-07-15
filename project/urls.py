"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    # Home and Authentication
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    
    # Task Management
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    # path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    # path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    # path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    # path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    
    # Product Management
    path('list_product/', views.list_product, name='list_product'),
    path('create_product/', views.create_product, name='create_product'),
    path('productos_comprados/<int:product_id>/', views.product_detail, name='product_detail'),
    path('productos_comprados/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('productos_comprados/<int:product_id>/update/', views.update_product, name='update_product'),
    
    # Sales Management
    path('list_venta/', views.list_venta, name='list_venta'),
    path('create_venta/', views.create_venta, name='create_venta'),
    path('productos_vendidos/<int:venta_id>/', views.venta_detail, name='venta_detail'),
    path('productos_vendidos/<int:venta_id>/delete/', views.delete_venta, name='delete_venta'),
    path('productos_vendidos/<int:venta_id>/update/', views.update_venta, name='update_venta'),

     path('fechas-productos-comprados/', views.fechas_productos_comprados, name='fechas_productos_comprados'),
     path('fechas_productos_vendidos/', views.fechas_productos_vendidos, name='fechas_productos_vendidos'),
     path('dinero-invertido/', views.fechas_dinero_invertido, name='dinero_invertido'),
]