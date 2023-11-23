from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('chat/<slug:slug>',views.chat,name='chat'),
    path('sendmsg',views.sendmsg,name='sendmsg'),
    path('recievemsg/<slug:slug>',views.recievemsg,name='recievemsg')
]