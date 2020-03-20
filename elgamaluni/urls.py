from django.urls import path
from elgamaluni.views import input_values_view
app_name = 'elgamaluni'
urlpatterns = [
    path('', input_values_view),
]