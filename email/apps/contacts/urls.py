from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
] 


