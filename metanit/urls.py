from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index),
    path("log_in/", views.log_in),
    path("registration/", views.registration),
    path("contacts/", views.contacts),
    path("user/", views.index_after),
]