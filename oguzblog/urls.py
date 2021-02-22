from django.contrib import admin
from django.urls import path
from oguzblog import views

app_name = "article"

urlpatterns = [
    path("portfoylo/",views.portfoylo,name = "portfoylo"),
    path("portfoylo2/",views.portfoylo2,name="portfoylo2"),
]