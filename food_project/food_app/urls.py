from django.urls import path
from .views import food_form, food_data, food_update, food_delete


urlpatterns = [
    path('form/', food_form, name='form_url'),
    path('data/', food_data, name='data_url'),
    path('update/<int:pk>/', food_update, name='update_url'),
    path('delete/<int:pk>/', food_delete, name='delete_url'),

]