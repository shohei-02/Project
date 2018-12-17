from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('game_list/', views.game_list, name='game_list'),
    path('game_list/<int:id>/', views.game_detail, name='game_detail'),
    path('game_list/new/', views.game_new, name='game_new'),
]