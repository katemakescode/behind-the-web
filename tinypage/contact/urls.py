from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('message-send/', views.message_send, name='message-send'),
]
