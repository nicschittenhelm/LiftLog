from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData),
    path("add/", views.addData),
    
    path("userdata/", views.user_data_list),
    path("userdata/add/", views.create_user_data),
    
    path("template/", views.get_workouttemplate),
    path("template/add/", views.create_workouttemplate),
]