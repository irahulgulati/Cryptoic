from django.urls import path
from elgamalre.views import input_value_view
app_name = 'elgamalre'
urlpatterns = [
    path('',input_value_view ,name = 'elgamalre'),
]