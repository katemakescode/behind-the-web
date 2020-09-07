from django.urls import path

from . import views

app_name = 'overtrick'
urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.SessionListView.as_view(), name='sessions-list'),
    path(
        'sessions/<club>/<int:year>/<int:month>/<int:day>/<str:time>',
        views.session_detail,
        name='sessions-detail'
    ),
]
