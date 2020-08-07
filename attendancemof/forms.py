from django import forms

from .models import Staff, StaffDetail, Attendance
from django.contrib.admin.widgets import AdminDateWidget


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class StaffDetailForm(forms.ModelForm):
    class Meta:
        model = StaffDetail
        fields = "__all__"


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
        widgets = {"attendance_date": forms.DateInput(format="%YYYY-%MM-%DD")}


# class DeductionForm(ModelForm):
#     class Meta:
#         model = TreasuryPurposes
#         fields = "__all__"
