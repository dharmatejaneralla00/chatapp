from django.contrib import auth, messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from . import models
# Create your views here.

def login(r):
    if r.user.is_authenticated:
        return redirect('home')
    else:
        if r.method == 'POST':
            username = r.POST['username']
            password = r.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(r,user)
                return redirect('home')
            else:
                messages.error(r,"username/password not correct")
        return render(r,'login.html')

def home(r):
    if r.user.is_authenticated:
        rooms = models.roomid.objects.filter(user1 = r.user.username) or models.roomid.objects.filter(user2 = r.user.username)
        return render(r,'home.html',{'rooms':rooms})
    else:
        return redirect('login')

def logout(r):
    auth.logout(r)
    return redirect('login')

def chat(r,slug):
    if r.user.is_authenticated:
        messages = models.message.objects.filter(slug=slug)
        return render(r,'chat.html',{'msgs':messages,'room':models.roomid.objects.get(roomid=slug)})
    else:
        return redirect('login')

def sendmsg(r):
    if r.method == 'POST':
        roomid = r.POST['roomid']
        user = r.POST['user']
        msg = r.POST['msg']
        models.message(roomid=roomid,msg=msg,user=user,slug=roomid).save()
        return JsonResponse({'res':True})

def recievemsg(r,slug):
    messages = models.message.objects.filter(slug=slug)
    return JsonResponse({'msgs':list(messages.values())})