from django.forms import ModelForm
from django.forms import forms
from .models import Stafflist
from .models import AttendanceT20
from .models import TreasuryPurposes
from django.contrib.admin.widgets import AdminDateWidget


class StaffForm(ModelForm):
    class Meta:
        model = Stafflist
        fields = "__all__"


class AttendanceForm(ModelForm):
    class Meta:
        model = AttendanceT20
        fields = "__all__"


class DeductionForm(ModelForm):
    class Meta:
        model = TreasuryPurposes
        fields = "__all__"
