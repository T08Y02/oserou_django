from django.urls import path

from .views import play, login, match

app_name = "oserou_forplay"

urlpatterns = [
    #play
    path('', play.index, name='index'),
    path('board', play.board, name='board'),
    path('board_refresh', play.boardRefresh, name='board_refresh'),
    path('result', play.result, name='result'),

    #match
    path('apply', match.matchApply, name='match_apply'),
    path('match/<int:first_player_id>/<int:second_player_id>', match.matchBoard, name='match_index'),
    path('match/board_refresh', match.matchBoardRefresh, name='match_board_refresh'),
    path('match/result/<int:first_player_id>/<int:second_player_id>', match.matchResult, name='match_result'),

    #ログイン周り
    path('signup/', login.signup_view.as_view(), name='signup'),
    path('login/', login.login_view.as_view(), name='login'),
    path('logout/', login.logout_view.as_view(), name='logout'),
    path('mypage/', login.user_view.as_view(), name='user'),
    path('other/', login.other_view.as_view(), name='other'),
]