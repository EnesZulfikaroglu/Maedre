from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import MessageForm, MessageToUserForm
from .models import Message
from user.models import Profile

# Create your views here.

@login_required(login_url="user:login")
def msgIndex(request):
    form = MessageForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, user_id=request.user)

    context = {
        "form": form,
        "profile": profile,
        }

    return render(request, "msgLayout.html", context)

@login_required(login_url="user:login")
def sendMessage(request):
    form = MessageForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, user_id=request.user)
    
    context = {
        "form": form,
        "profile": profile,
        }

    if form.is_valid():
        try:
            msg = form.save(commit=False)


            msg.sender = request.user
            
            receiverUser = User.objects.get(username= msg.username)
            msg.reciever_id = receiverUser.id

            msg.save()

            messages.success(request, "Mesaj Gönderildi")
            return redirect("/message")

        except:
            messages.info(request, "Hatalı kullanıcı adı!")

    return render(request, "sendMessage.html", context)

@login_required(login_url="user:login")
def sendMessageToUser(request,id):
    user = get_object_or_404(User, id= id)
    form = MessageToUserForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, user_id= id)
    
    context = {
        "form" : form,
        "profile" : profile,
        "username" : user.username,
        }

    if form.is_valid():
        msg = form.save(commit=False)


        msg.sender = request.user
        
        receiverUser = user
        msg.reciever_id = receiverUser.id

        msg.save()

        messages.success(request, "Mesaj Gönderildi")
        return redirect("/message")

    return render(request, "sendMessageToUser.html", context)

@login_required(login_url="user:login")
def inbox(request):
    inbox = Message.objects.filter(reciever_id= request.user.id).order_by("-created_date")
    profile = get_object_or_404(Profile, user_id=request.user)
    
    context = {
        "inboxMessages": inbox,
        "profile": profile,
        }

    return render(request, "inbox.html", context)

@login_required(login_url="user:login")
def outbox(request):
    inbox = Message.objects.filter(sender_id= request.user.id).order_by("-created_date")
    profile = get_object_or_404(Profile, user_id=request.user)
    
    context = {
        "inboxMessages": inbox,
        "profile": profile,
        }

    return render(request, "outbox.html", context)

@login_required(login_url="user:login")
def details(request,id):
    msg = get_object_or_404(Message, id= id)
    profile = get_object_or_404(Profile, user_id=request.user)
    
    context = {
        "msg": msg,
        "profile": profile,
        }

    return render(request, "msgDetails.html", context)