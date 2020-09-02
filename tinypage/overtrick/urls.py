from django.urls import path

from . import views

app_name = 'overtrick'
urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.session_list, name='sessions-list'),
    path(
        # 'sessions/<str:club>/<int:year>/<int:month>/<int:day>/<str:time>/',
        'sessions/<int:session_id>/',
        views.session_detail,
        name='sessions-detail'
    ),
]
