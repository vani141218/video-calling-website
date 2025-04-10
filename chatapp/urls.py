from django.urls import path
from . import views

urlpatterns = [
    path('',views.lobby),
    path('chatroom/',views.chatroom),
    path('generatetoken/',views.generatetoken),
    path('create_member/',views.createMember),
    path('get_member/',views.getMember),
    
]
