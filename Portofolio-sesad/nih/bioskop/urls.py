from django.urls import path
from bioskop import views

urlpatterns = [
    path('',views.home,name='home'), 
]
