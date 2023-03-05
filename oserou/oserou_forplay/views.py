import asyncio
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from oserou_forplay.modules import placestone
from django.urls import reverse
import numpy as np


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the play index.")

def board(request):
    template = loader.get_template('oserou_forplay/ban.html')
    context = {
        'board_state_key': [[1 for i in range(8)] for j in range(8)],
    }
    return HttpResponse(template.render(context, request))

def boardRefresh(request):
    #board_stateは文字列として渡されているので注意
    color = int(request.POST.get('color'))
    selected_collumn = int(request.POST.get('selected_collumn'))
    selected_row = int(request.POST.get('selected_row'))
    board_state = request.POST.get('board_state')
    board_state = board_state.split(",")
    board_state = np.array(board_state, dtype=np.int64).reshape(8, 8)
    new_board_state = placestone.board_placestone(board_state, selected_row, selected_collumn, color)
    new_board_state = new_board_state.tolist()
    d = {
        'new_board_state': new_board_state,
    }
    return JsonResponse(d)

