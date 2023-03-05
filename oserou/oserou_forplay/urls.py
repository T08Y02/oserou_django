from django.urls import path

from . import views

app_name = "oserou_forplay"

urlpatterns = [
    path('', views.index, name='index'),
    path('board', views.board, name='board'),
    path('board_refresh', views.boardRefresh, name='board_refresh'),
]