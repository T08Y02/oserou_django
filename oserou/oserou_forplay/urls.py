from django.urls import path

from .views import play, login

app_name = "oserou_forplay"

urlpatterns = [
    path('', play.index, name='index'),
    path('board', play.board, name='board'),
    path('board_refresh', play.boardRefresh, name='board_refresh'),
    path('result', play.result, name='result'),

    #ログイン周り
    path('signup/', login.signup_view.as_view(), name='signup'),
    path('login/', login.login_view.as_view(), name='login'),
    path('logout/', login.logout_view.as_view(), name='logout'),
    path('mypage/', login.user_view.as_view(), name='user'),
    path('other/', login.other_view.as_view(), name='other'),
]