from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListView, name='list_inventory'),
    path('inventory/create', views.InventoryCreate, name='create_inventory'),
    path('inventory/edit/<int:id>', views.InventoryEdit, name='edit_inventory'),

    path('production/', views.ProductionListView, name='list_production'),
    path('production/create', views.ProductionCreate, name='create_production'),
    path('production/edit/<int:id>', views.ProductionEdit, name='edit_production'),

    path('procurement/', views.ProcurementListView, name='list_procurement'),
    path('procurement/create', views.ProcurementCreate, name='create_procurement'),
    path('procurement/edit/<int:id>', views.ProcurementEdit, name='edit_procurement')

]