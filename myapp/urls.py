from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.idcard_home),
    path('pak_id_card', views.pak_idcard),
    path('balaji_id_card', views.balaji_idcard),
    path('temp/',views.temp,name='temp'),
    path('pak_idcard_download/<int:pk>/', views.pak_idcard_download, name='pak_idcard_download'),
    path('balaji_idcard_download/<int:pk>/', views.balaji_idcard_download, name='balaji_idcard_download'),
]
