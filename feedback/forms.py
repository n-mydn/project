from django.forms import ModelForm
from .models import Feedback,Department,FeedbackStatusHistory

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["IdCompany","Name","Surname","Email","PhoneNumber","IdDepartment","IdFeedbackType","IdFeedbackSource","IdFeedbackReason","IdFeedbackPersonel","Content","Photo"]

class AdminFeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields=["IdFeedbackStatus","IdFeedbackPriorityLevel","LastSolveDate"]

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ["status",]


class StatusHistoryForm(ModelForm):
    class Meta:
        model = FeedbackStatusHistory
        fields = ["history_note","history_file"]


class StatusForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["IdFeedbackStatus",]
