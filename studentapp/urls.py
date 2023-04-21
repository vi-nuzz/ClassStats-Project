from django.urls import path
from .views import *

urlpatterns = [
    path('stud_details/',stud_details),
    path('stud_display/',stud_display),
]
