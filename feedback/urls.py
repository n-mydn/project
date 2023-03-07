from django.urls import path
from . import views

app_name="feedback"

urlpatterns = [
    path('feedback/',views.feedback,name="feedback"),
    path('feedback_detail/<int:id>',views.feedback_detail,name="feedback_detail"),
    path('feedbackdepartment_update/<int:id>',views.feedbackdepartment_update,name="feedbackdepartment_update"),

    path('admin_feedback_detail/<int:id>',views.admin_feedback_detail,name="admin_feedback_detail"),
    path('feedback_admin_update/<int:id>',views.feedback_admin_update,name="feedback_admin_update"),
    path('admin_department_islemde/<int:id>',views.admin_department_islemde,name="admin_department_islemde"),
    path('admin_department_cozuldu/<int:id>',views.admin_department_cozuldu,name="admin_department_cozuldu"),
    path('admin_department/<int:id>',views.admin_department,name="admin_department"),
    path('admin_all_department',views.admin_all_department,name="admin_all_department"),
    path('aktif_pasif_update/<int:id>',views.aktif_pasif_update,name="aktif_pasif_update"),
  

    path('d_admin_index',views.d_admin_index,name="d_admin_index"),
    path('d_admin_feedback_detail/<int:id>',views.d_admin_feedback_detail,name="d_admin_feedback_detail"),
    path('feedback_status_update/<int:id>',views.feedback_status_update,name="feedback_status_update"),
    path('files_read/<int:id>',views.files_read,name="files_read"),
]

"""
  path('feedback_status_create/<int:id>',views.feedback_status_create,name="feedback_status_create"),
"""