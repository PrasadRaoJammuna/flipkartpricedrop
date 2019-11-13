from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add_url/',views.add_url,name='add_url'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('dashboard/',views.dashboard,name='dashboard'),
    #path('email/',views.send_mail,name='email'),
    
]
