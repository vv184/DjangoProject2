from django.urls import path

from .views import (
    create_property,
    property_list,
    edit_property,
    delete_property,
    toggle_property,
)

urlpatterns = [
    path('', property_list, name='property_list'),
    path('create/', create_property, name='create_property'),
    path('<int:property_id>/edit/', edit_property, name='edit_property'),
    path('<int:property_id>/delete/', delete_property, name='delete_property'),
    path('<int:property_id>/toggle/', toggle_property, name='toggle_property'),
]
