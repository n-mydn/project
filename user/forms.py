from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserAddProfile

class RegisterFrom(forms.Form):
    name = forms.CharField(max_length=30,label="AD")
    last_name= forms.CharField(max_length=15, label="SOYAD")
    email = forms.EmailField(label="E-POSTA")
    password = forms.CharField(max_length=20,label="PAROLA", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="PAROLA DOĞRULA",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ["name","last_name","email","password","confirm"]

        def clean(self):
            name = self.cleaned_data.get("name")
            last_name = self.cleaned_data.get("last_name")
            email = self.cleaned_data.get("email")
            password = self.cleaned_data.get("password")
            confirm = self.cleaned_data.get("confirm")

            if password and confirm and password != confirm:
                raise forms.ValidationError('Parolalar Eşleşmiyor')
        
            values = {
                "password":password,
                "email":email,
                "last_name":last_name,
                "name":name,
                }

            return values

class RegisterAddForm(ModelForm):
    class Meta:
        model = UserAddProfile
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)