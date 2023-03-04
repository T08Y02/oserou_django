import asyncio
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from oserou_forplay.modules import placestone
from django.urls import reverse
import numpy as np
import json


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
    board_state = request.POST.get('board_state')
    board_state = board_state.split(",")
    board_state = np.array(board_state).reshape(8, 8)
    selected_collumn = int(request.POST.get('selected_collumn'))
    selected_row = int(request.POST.get('selected_row'))
    color = int(request.POST.get('color'))
    new_board_state = placestone.board_placestone(board_state, selected_row, selected_collumn, color)
    template = loader.get_template('oserou_forplay/ban.html')
    context = {
        'board_state_key': new_board_state,
    }
    return HttpResponse(template.render(context, request))

