import asyncio
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the play index.")

async def board(request):
    template = loader.get_template('oserou_forplay/ban.html')
    context = {
        'board_state_key': [[1 for i in range(8)] for j in range(8)],
    }
    return HttpResponse(template.render(context, request))
