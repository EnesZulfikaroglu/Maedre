from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ProfileForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from ilan.models import Ilan

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form" : form
    }

    second_form = ProfileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        profile = second_form.save(commit=False)

        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")


        newUser = User(username=username, email= email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)

        profile.user = request.user
        profile.email = email
        profile.photo = 'Photo/defaultProfilePic.png'
        profile.save()

        messages.success(request, "Kayıt Başarılı!")

        return redirect("index")

        messages.warning(request, "Kullanıcı adı başkası tarafından alınmış")
        return render(request, "register.html", context)

    return render(request, "register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username, password= password)

        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı")
            return render(request, "login.html", context)
        
        messages.success(request,"Başarıyla giriş yapıldı")
        login(request, user)
        return redirect("index")
    
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı")
    return redirect("index")

def showProfile(request, id):
    user = get_object_or_404(User, id= id)

    profile = user.profile.first()

    ilans = Ilan.objects.filter(owner= id).order_by('-created_date')

    context = {
        "profile" : profile,
        "user" : user,
        "ilans" : ilans
        }

    return render(request, "profile.html", context)

@login_required(login_url="user:login")
def updateProfile(request, id):

    if id == request.user.id:
        profile = get_object_or_404(Profile, user_id= id)

        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        
        context = {
            "form": form,
        }

        if form.is_valid():
            new_profile = form.save(commit=False)

            new_profile.user = request.user

            new_profile.save()
            messages.success(request,"Profil başarıyla güncellendi")
            return redirect("/user/profile/{}".format(id))

        return render(request, 'updateProfile.html', context)

    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "index.html")
