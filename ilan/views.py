from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import IlanForm
from .models import Ilan, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url="user:login")
def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url="user:login")
def addIlan(request):
    form = IlanForm(request.POST or None, request.FILES or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        ilan = form.save(commit= False)
        ilan.owner = request.user
        ilan.save()

        messages.success(request,"İlan başarıyla eklendi")

        return redirect("ilan:dashboard")

    return render(request, "addIlan.html", context)

@login_required(login_url="user:login")
def showIlans(request):
    ilans = Ilan.objects.filter(owner= request.user).order_by('-created_date')

    context = {
        "ilans" : ilans
    }
    
    return render(request, "showIlans.html", context)

def detail(request,id):
    ilan = get_object_or_404(Ilan, id= id)
    comments = ilan.comments.all()
    
    context = {
        "ilan" : ilan,
        "comments" : comments
    }
    
    return render(request, "details.html", context)

@login_required(login_url="user:login")
def updateIlan(request,id):
    ilan = get_object_or_404(Ilan, id= id)
    
    if request.user.id == ilan.owner.id:
        form = IlanForm(request.POST or None, request.FILES or None, instance= ilan)

        context = {
            "form" : form
        }

        if form.is_valid():
            ilan = form.save(commit= False)
            ilan.save()

            messages.success(request,"İlan başarıyla güncellendi")
            return redirect("ilan:showIlans")

        return render(request, "update.html", context)

    else:
        messages.info(request,"Bu ilanı güncelleme yetkiniz yok!")
        return redirect("index")

@login_required(login_url="user:login")
def deleteIlan(request,id):
    ilan = get_object_or_404(Ilan, id= id)

    if request.user.id == ilan.owner.id:
        ilan.delete()
        messages.success(request,"İlan başarıyla silindi")
        return redirect("ilan:showIlans")
        
    else:
        messages.info(request,"Bu ilanı silme yetkiniz yok!")
        return redirect("index")

def showAll(request):
    keyword = request.GET.get("keyword")

    if keyword:
        ilans = Ilan.objects.filter(title__contains= keyword)
        return render(request, "showAll.html", {"ilans" : ilans})

    ilans = Ilan.objects.all().order_by('-created_date')
    return render(request, "showAll.html", {"ilans" : ilans})

@login_required(login_url="user:login")
def addComment(request,id):
    ilan = get_object_or_404(Ilan, id= id)

    if request.method == "POST":
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_content= comment_content)

        newComment.ilan = ilan
        newComment.comment_user = request.user

        newComment.save()

        return redirect(reverse("ilan:details", kwargs={"id":id}))
