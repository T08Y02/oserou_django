from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from oserou_forplay.modules import placestone, calcscore, findinvalidinput as fii, calcresult
from django.urls import reverse
import numpy as np
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..models import PlayerUser, Result
from datetime import datetime

@login_required
def matchApply(request):
    all_players = PlayerUser.objects.all()
    context = {
        'players': all_players
    }
    template = loader.get_template('oserou_forplay/apply.html')
    return HttpResponse(template.render(context, request))

@login_required
def matchBoard(request, first_player_id, second_player_id):
    first_player = PlayerUser.objects.filter(pk = first_player_id).get()
    second_player = PlayerUser.objects.filter(pk = second_player_id).get()
    context = {
        'first_player': first_player,
        'second_player': second_player,
        'board_state_key': [[1 for i in range(8)] for j in range(8)],
    }
    template = loader.get_template('oserou_forplay/match.html')
    return HttpResponse(template.render(context, request))

@login_required
def matchBoardRefresh(request, first_player_id, second_player_id):
    #board_stateは文字列として渡されているので注意
    color = int(request.POST.get('color'))
    selected_collumn = int(request.POST.get('selected_collumn'))
    selected_row = int(request.POST.get('selected_row'))
    board_state = request.POST.get('board_state')
    board_state = board_state.split(",")
    board_state = np.array(board_state, dtype=np.int64).reshape(8, 8)                
    #valid 0:OK, 1:not valid input, 2:pass, 3:finish, 4:invalid pass
    valid = fii.checkValid(board_state, selected_row, selected_collumn, color)
    if valid == 0:
        new_board_state = placestone.board_placestone(board_state, selected_row, selected_collumn, color)
        board_state = new_board_state
    first_player = PlayerUser.objects.filter(pk = first_player_id).get()
    second_player = PlayerUser.objects.filter(pk = second_player_id).get()
    d = {
        'new_board_state': board_state.tolist(),
        'return_code' : valid,
        'first_player': first_player,
        'second_player': second_player,
    }
    return JsonResponse(d)


@login_required
def matchResult(request, first_player_id, second_player_id):
    board_state = request.POST.get('result')
    board_state = board_state.split(",")
    board_state = np.array(board_state, dtype=np.int64).reshape(8, 8)
    [winner, matchscore] = calcresult.winner(board_state)
    template = loader.get_template('oserou_forplay/result.html')
    context = {
        'winner' : winner,
        'score' : matchscore,
        'first_player' : PlayerUser.objects.filter(pk = first_player_id).get(),
        'second_player': PlayerUser.objects.filter(pk = second_player_id).get()
    }

    #データベースへの保存
    if winner == "first player":
        winner_instance = PlayerUser.objects.filter(pk = first_player_id).get()
        loser_instance = PlayerUser.objects.filter(pk = second_player_id).get()
    elif winner == "second player":
        winner_instance = PlayerUser.objects.filter(pk = second_player_id).get()
        loser_instance = PlayerUser.objects.filter(pk = first_player_id).get()
    else:
        print("draw")
        return HttpResponse(template.render(context, request))
    Result.objects.create(winner_id = winner_instance, loser_id = loser_instance,
                          score = matchscore, created_at = datetime.now())
    return HttpResponse(template.render(context, request))

