from django import forms
from .models import Profile

class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 20, label= "Kullanıcı Adı")
    email = forms.CharField(max_length= 50, label= "E-Mail")
    password = forms.CharField(max_length= 20, label= "Parola", widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label= "Parola (tekrar)", widget= forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor")

        values = {
            "username" : username,
            "email"    : email,
            "password" : password,
        }
        
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı:")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "name", "surname", "about", "instagram", "twitter", "facebook", "high_school", "university"]