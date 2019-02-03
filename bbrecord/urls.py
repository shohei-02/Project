from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('game_list/', views.game_list, name='game_list'),
    path('game_list/<int:id>/', views.game_detail, name='game_detail'),
    path('game_list/new/', views.game_new, name='game_new'),
    path('game_list/<int:id>/edit/', views.game_edit, name='game_edit'),
    path('game_list/game_delete/<int:id>/', views.game_delete, name='game_delete'),
    path('stats_list', views.stats_list, name='stats_list'),
]
