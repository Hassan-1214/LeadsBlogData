from django.urls import path
from .views import *


urlpatterns = [
    path('blog/', BlogApiView.as_view(), name='blog'),
   
    
]
