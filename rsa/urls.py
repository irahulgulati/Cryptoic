from django.urls import path
from rsa.views import input_values_view
app_name = 'rsa'
urlpatterns = [
    path('',input_values_view ,name = 'rsa'),
]
