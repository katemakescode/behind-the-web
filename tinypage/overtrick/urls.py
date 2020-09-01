from django.urls import path

from . import views

app_name = 'overtrick'
urlpatterns = [
    path('', views.index, name='index'),
]
