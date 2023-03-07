from django.shortcuts import render,redirect,get_object_or_404
from .models import Feedback,Department,FeedbackStatusHistory
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm,AdminFeedbackForm,DepartmentForm,StatusHistoryForm,StatusForm
from django.contrib import messages
from django.utils.timezone import now
from user.models import UserAddProfile
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def zaman(feedback):
        liste = list()
        time = now() - feedback.FeedbackOpenDate
        for t in str(time):
            liste.append(t)
        if liste[2] == "d":
            time = liste[0] + " gün"
        elif liste[3]=="d":
            time = liste[0]+liste[1]+" gün"
        elif liste[2] == ":":
            time = time + "saat"
        elif liste[2]=="m":
            time = liste[0] +" ay"
        elif liste[3]=="m":
            time = liste[0]+liste[1]+" ay"
        feedback.DurationTime = time
        feedback.save()

# --------------- Departman Admini ---------------
@login_required(login_url="user:login")
def d_admin_index(request):
    k_user = request.user
    d_user = UserAddProfile.objects.filter(user=k_user).first()
    department = d_user.user_department
    feedbacks_list = Feedback.objects.filter(IdDepartment=department.id,IdFeedbackStatus=2)
 
    paginator = Paginator(feedbacks_list, 1)  # Show 5 contacts per page
    page = request.GET.get('sayfa')
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        feedbacks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        feedbacks = paginator.page(paginator.num_pages)

    sayı = 0
    for feedback in feedbacks_list:
        zaman(feedback)
        if FeedbackStatusHistory.objects.filter(history_feedback_id=feedback.id).first()==None and feedback.FeedbackClosedDate > feedback.LastSolveDate:
            sayı +=1
           

    keyword = request.GET.get("keyword") 
    if keyword:
        feedbacks = Feedback.objects.filter(
            Q(IdDepartment=department.id),
            Q(IdFeedbackStatus = 2),
            Q(IdFeedbackPriorityLevel__name__icontains=keyword)
        ).distinct()

    context = {
        "department":department,
        "feedbacks":feedbacks,
        "sayı":sayı,
    } 
    return render(request,"department_admin/index.html",context)


@login_required(login_url="user:login")
def d_admin_feedback_detail(request,id):
    feedback = Feedback.objects.filter(id=id).first()
    feedback_status = FeedbackStatusHistory.objects.filter(history_feedback=id).first()
    print(feedback.FeedbackClosedDate-feedback.FeedbackOpenDate)
    zaman(feedback) #olmazsa zaman altında olanı kopyala yapıştır!
    context = {
        "feedback":feedback, 
        "feedback_status":feedback_status,
    }
    return render(request,"department_admin/feedback_detail.html",context)


@login_required(login_url="user:login")
def feedback_status_update(request,id):
    feedback = Feedback.objects.filter(id=id).first()
    feedback_status = FeedbackStatusHistory.objects.filter(history_feedback = id).first()
    form = StatusHistoryForm(request.POST or None,request.FILES or None,instance=feedback_status)
    context={
        "form":form,
        "feedback_status":feedback_status,
    }
    if form.is_valid():
        status = form.save(commit = False)
        status.history_feedback_id = id
        status.history_status_id = feedback.IdFeedbackStatus.id
        status.history_department_id = feedback.IdDepartment.id
        status.history_user = request.user
        status.save()
        messages.success(request,"Talep-Şikayet Yanıtları Oluşturuldu.")
        return redirect("feedback:d_admin_index")

    return render(request,"department_admin/feedback_status.html",context)


@login_required(login_url="user:login")
def files_read(request,id):
    feedback_status = FeedbackStatusHistory.objects.filter(id=id).first()
    with open(feedback_status.history_file.path,"r",encoding="utf-8") as file:
        f = file.read()
        return render(request,"files_read.html",{"f":f})

#-----------------------------------------------------------------------------
def index(request):
    return render(request,"index.html")
    """
    f_department = "Acil Servis"
    feedbacks = Department.objects.get(name=f_department).feedback_set.all()
    context={
        "feedbacks":feedbacks
    }
    return render(request,"index.html",context)
    """


login_required(login_url="user:login")
def feedback(request):
    form = FeedbackForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        id = request.POST["IdDepartment"]
        department = Department.objects.filter(id=id).first()
        if department.status == "Pasif" :
            messages.info(request,"{} Departmanı Şu An Aktif Değildir!".format(department.name))
            messages.info(request,"Departman Seçiminizi Tekrar Kontrol Ediniz!")
            return render(request,"feedback_create.html",{"form":form})
        form.save()
        messages.success(request,"Talep-Şikayet Başarıyla Oluşturuldu.")
        return redirect("index")
    return render(request,"feedback_create.html",{"form":form})


@login_required(login_url="user:login")
def all_department(request):
    departments = Department.objects.all()
    context = {
        "departments":departments
    }
    return render(request,"all_department.html",context)


@login_required(login_url="user:login")
def department_detail(request,id):
    dprt = Department.objects.filter(id=id).first()
    feedbacks = Feedback.objects.filter(IdDepartment=id)
    context = {
        "dprt":dprt,
        "feedbacks":feedbacks,
    }
    return render(request,"department_detail.html",context)

@login_required(login_url="user:login")
def feedback_detail(request,id):
    feedback = Feedback.objects.filter(id=id).first()
    context={
        "feedback":feedback
    }
    return render(request,"feedback_detail.html",context)

@login_required(login_url="user:login")
def feedbackdepartment_update(request,id):
    pass


# ----------------- ADMİN BÖLÜMÜ -----------------

@login_required(login_url="user:login")
def admin_all_department(request):
    departments = Department.objects.all()
    return render(request,"admin/all_department.html",{"departments":departments})

@login_required(login_url="user:login")
def admin_feedback_detail(request,id):
    feedback = Feedback.objects.filter(id=id).first()
    feedback_status = FeedbackStatusHistory.objects.filter(history_feedback=id).first()
    context = {
        "feedback":feedback,
        "feedback_status":feedback_status, 
    }
    return render(request,"admin/feedback_detail.html",context)


@login_required(login_url="user:login")
def admin_department(request,id):
    dprt = Department.objects.filter(id=id).first()
    f = Feedback.objects.filter(IdDepartment=id)
    feedbacks_list = Feedback.objects.filter(IdDepartment=id,IdFeedbackStatus=1)

    paginator = Paginator(feedbacks_list, 1)  # Show 5 contacts per page
    page = request.GET.get('sayfa')
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        feedbacks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages.warning(request,"Geçerli olmayan sayfa numarası!")
        feedbacks = paginator.page(paginator.num_pages)

    context = {
        "dprt":dprt,
        "feedbacks":feedbacks,
        "f":f,
        } 
    return render(request,"admin/admin_department.html",context)


@login_required(login_url="user:login")
def admin_department_islemde(request,id):
    dprt = Department.objects.filter(id=id).first()
    feedbacks_list = Feedback.objects.filter(IdDepartment=id,IdFeedbackStatus=2)

    paginator = Paginator(feedbacks_list, 1)  # Show 5 contacts per page
    page = request.GET.get('sayfa')
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        feedbacks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages.warning(request,"Geçerli olmayan sayfa numarası!")
        feedbacks = paginator.page(paginator.num_pages)

    liste = list()
    for feedback in feedbacks_list:
        feedback_status = FeedbackStatusHistory.objects.filter(
            Q(history_feedback_id=feedback.pk),
            Q(history_department_id=id),
            Q(history_status_id=2)
        ).distinct()
        if feedback_status.first() != None:
            liste.append(feedback_status)
    context = {
        "dprt":dprt,
        "feedbacks":feedbacks,
        "liste":liste,
        "sayı":len(liste),
    }
    return render(request,"admin/admin_department_islemde.html",context)

@login_required(login_url="user:login")
def admin_department_cozuldu(request,id):
    dprt = Department.objects.filter(id=id).first()
    feedbacks_list = Feedback.objects.filter(IdDepartment=id,IdFeedbackStatus=3)
    paginator = Paginator(feedbacks_list, 1)  # Show 5 contacts per page
    page = request.GET.get('sayfa')
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        feedbacks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages.warning(request,"Geçerli olmayan sayfa numarası!")
        feedbacks = paginator.page(paginator.num_pages)

    context = {
        "dprt":dprt,
        "feedbacks":feedbacks
    }
    return render(request,"admin/admin_department_cozuldu.html",context)


@login_required(login_url="user:login")
def aktif_pasif_update(request,id):
    department = Department.objects.filter(id=id).first()
    name = department.name
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        department = form.save(commit = False)
        if form.has_changed() == False :
            messages.info(request,"Departmanın Durumu Değişmedi.")
            return render(request,"admin/aktif_pasif_update.html",{"form":form})

        department.name = name
        department.save()
        messages.success(request,"Departmanın Durumu Güncellendi.")
        return redirect("feedback:admin_all_department")
        
    return render(request,"admin/aktif_pasif_update.html",{"form":form})


@login_required(login_url="user:login")
def feedback_admin_update(request,id):
    feedback = Feedback.objects.get(id=id)
    form = AdminFeedbackForm(request.POST or None,instance=feedback)
    feedback_status = FeedbackStatusHistory.objects.filter(history_feedback=id).first()
    status_form = StatusForm(request.POST or None,instance=feedback)
    context = {
        "form":form,
        "feedback_status":feedback_status,
        "status_form":status_form,
    }
    if form.is_valid():
        feedback = form.save(commit=False)
        if feedback.IdFeedbackStatus.id != 2:
            messages.info(request,"Talep-Şikayet Durumu 'İşlemde' Olmalıdır!")
            return render(request,"admin/feedback_admin_update.html",context)
        if feedback.LastSolveDate < feedback.FeedbackClosedDate :
            messages.info(request,"Talep-Şikayet İçin Gerekli Zaman Geçmiş Zaman Olamaz!")
            return render(request,"admin/feedback_admin_update.html",context)
            
        zaman(feedback) #olmazsa zaman altında olanı kopyala yapıştır!
        messages.success(request,"Talep-Şikayet Bilgileri Güncellendi.")
        return redirect("feedback:admin_department",id=feedback.IdDepartment.id)
    
    if status_form.is_valid():
        status = status_form.save(commit=False)
        if status.IdFeedbackStatus.id != 3:
            messages.info(request,"Talep-Şikayet Durumu 'ÇÖZÜLDÜ' Olmalıdır!")
            return render(request,"admin/feedback_admin_update.html",context)
        status.save()
        zaman(feedback) #olmazsa zaman altında olanı kopyala yapıştır!
        """
        an = datetime.now()
        time = an.day - feedback.FeedbackOpenDate.day
        feedback.DurationTime = time
        feedback.save()
        """
        feedback_status.history_status_id = 3
        feedback_status.save()
        messages.success(request,"Talep-Şikayet Durumu Güncellendi.")
        return redirect("feedback:admin_department",id=feedback.IdDepartment.id)

    return render(request,"admin/feedback_admin_update.html",context)

