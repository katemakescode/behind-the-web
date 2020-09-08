from django.urls import path

from . import views

urlpatterns = [
    path('message-send/', views.message_send),
]
