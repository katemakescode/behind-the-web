from django.urls import path

from . import views

urlpatterns = [
    path('subscribe/', views.subscriber_create),
    path('subscriber/<int:subscriber_id>/', views.subscriber_get),
]
