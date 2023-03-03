import asyncio
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the play index.")

async def ban(request):
    #await asyncio.sleep(1)
    template = loader.get_template('oserou_forplay/ban.html')
    return HttpResponse(template.render())
