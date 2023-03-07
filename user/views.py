from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
# Create your views here.


def login(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        auth_login(request,user)

        if request.user.username == "admin":
            return redirect("feedback:admin_all_department")
        elif request.user.username == "acil_servis_admin" or request.user.username=="algoloji_admin" or request.user.username == "aile_hekimliği_admin" or request.user.username=="amatem_admin":
            return redirect("feedback:d_admin_index")
        elif request.user.username == "anesteziyoloji_admin" or request.user.username =="beyin_sinir_admin" or request.user.username == "onkoloji_admin" or request.user.username == "çocuk_admin":
            return redirect("feedback:d_admin_index")
        elif request.user.username == "cildiye_admin" or request.user.username=="diş_admin" or request.user.username=="endodonti_admin" or request.user.username=="endokrin_admin" or request.user.username=="enfeksiyon_admin":
            return redirect("feedback:d_admin_index")  
        elif request.user.username=="rehabilitasyon_admin" or request.user.username=="gastroenteroloji_admin" or request.user.username=="gelişimsel_pediatri_admin" or request.user.username=="cerrahi_admin" or request.user.username=="göz_admin":
            return redirect("feedback:d_admin_index")
        elif request.user.username =="hematoloji_admin" or request.user.username=="dahiliye_admin" or request.user.username=="immünoloji_alerji_admin" or request.user.username=="mesleki_hastalıklar_admin" or request.user.username=="kadın_hastalıkları_admin":
            return redirect("feedback:d_admin_index")
        elif request.user.username == "kalp_damar_admin" or request.user.username=="kbb_admin" or request.user.username=="nefroloji_admin" or request.user.username=="nöroloji_admin" or request.user.username=="ordodonti_admin" or request.user.username=="perinatoloji_admin":
            return redirect("feedback:d_admin_index")
        elif request.user.username =="plastik_cerrahi_admin" or request.user.username=="psikiyatri_admin" or request.user.username=="üroloji_admin" or request.user.username=="radyoloji_admin":
            return redirect("feedback:d_admin_index") 
        else:
            return redirect("index")

    return render(request,"login.html",context)

"""
def d_login(request):
    form = LoginForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola hatalı")
            return render(request,"d_login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        auth_login(request,user)
        return redirect("feedback:d_admin_index")
    return render(request,"department_admin/login.html",context)

def a_login(request):
    form = LoginForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola hatalı")
            return render(request,"d_login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        auth_login(request,user)

        if request.user.username == "admin":
            return redirect("feedback:admin_all_department")
        elif request.user.username == "acil_servis_admin":
            return redirect("feedback:d_admin_index")
            
    return render(request,"admin/login.html",context)
"""

def logout(request):
    auth_logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız.")
    return redirect("index")