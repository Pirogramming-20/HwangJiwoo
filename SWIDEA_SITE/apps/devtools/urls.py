from django.urls import path
from .views import *

app_name = "devtools"

urlpatterns = [
    path('list/', devtools_list, name='list'),
    path('create/', devtools_create, name='create'),
    path('detail/<int:pk>', devtools_detail, name='detail'),
    path('delete/<int:pk>', devtools_delete, name='delete'),
    path('update/<int:pk>', devtools_update, name='update'),
]