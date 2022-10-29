from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("charge/", views.charge, name="charge"),
    path("success/<str:args>/", views.successMsg, name="successMsg")
]

urlpatterns += staticfiles_urlpatterns()