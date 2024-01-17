from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name="create"),
    path('detail/<int:pk>', detail, name='detail'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
    path('update_interest/', update_interest, name='update_interest'),
    path('update_star/<int:pk>', update_star, name='update_star'),
    path('update_star2/<int:pk>', update_star2, name='update_star2'),
]