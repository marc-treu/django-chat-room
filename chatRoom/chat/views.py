from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "chat/index.html")


@csrf_exempt
def login(request):
    nick_name = request.POST.get('nickname', '')
    request.session['nickname'] = nick_name
    return HttpResponse("OK")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
