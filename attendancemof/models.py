from django.contrib.auth.models import AbstractUser
from django.db import models

BAND = (
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("H", "H"),
    ("I", "I"),
    ("J", "J"),
    ("K", "K"),
    ("L", "L"),
    ("M", "M"),
    ("N", "N"),
    ("O", "O"),
    ("P", "P"),
    ("Q", "Q"),
    ("R", "R"),
    ("S", "S"),
)

DIVISION = (
    ("CSD", "Corporate Services Division"),
    ("CEO", "Office of the CEO"),
    ("OM", "Office of the Minister"),
    ("IT", "Information Technology and Communication Division"),
    ("FFD", "Financial Framework Division"),
    ("PD", "Procurement Division"),
    ("TD", "Treasury Division"),
    ("BD", "Budget Division"),
    ("APD", "Aid and Projects Division"),
    ("EFPD", "Economic and Fiscal Policy Division"),
    ("RD", "Resilience Division"),
    ("EUA", "SUB EUA"),
    ("VAVAU", "SUB VAVAU"),
    ("HAAPAI", "SUB HAAPAI"),
)

ATTENDANCE_TYPE = (
    ("ON_DUTY", "On Duty"),
    ("LATE", "Late"),
    ("CASUAL_LEAVE", "Casual Leave"),
    ("ANNUAL_LEAVE", "Annual Leave"),
    ("SICK_LEAVE", "Sick Leave"),
    ("IN_LIEU", "In Lieu"),
    ("NOP", "NOP"),
    ("WOP", "WOP"),
)


class User(AbstractUser):
    # A User can be of different type, like a Staff User
    class Types(models.TextChoices):
        STAFF = "STAFF", "Staff"

    base_type = Types.STAFF

    type = models.CharField(max_length=50, choices=Types.choices, default=base_type)
    name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class StaffDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    band = models.CharField(max_length=255, blank=True, choices=BAND)
    position = models.CharField(max_length=255, blank=True)
    division = models.CharField(max_length=255, blank=True, choices=DIVISION)

    def __str__(self):
        return self.user.username


class Staff(User):
    base_type = User.Types.STAFF

    class Meta:
        proxy = True

    @property
    def details(self):
        return self.staffdetail


class Attendance(models.Model):
    type = models.CharField(max_length=50, choices=ATTENDANCE_TYPE)
    attendance_date = models.DateField()
    request_from = models.TimeField(null=True)
    request_to = models.TimeField(null=True)
    remarks = models.CharField(null=True, blank=True, max_length=500)
    staff = models.ForeignKey(
        "StaffDetail",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="attendances",
    )

    def __str__(self):
        return f"{self.type} for {self.staff}"


# class TreasuryPurposes(AttendanceT20):
#     t_id = models.AutoField(default="1", primary_key=True)
#     Time_Out = models.TimeField(null=True)
#     Late_hours = models.TimeField(null=True)
#     Overtime_In = models.TimeField(null=True)
#     Overtime_Out = models.TimeField(null=True)
#     Deduction_Hours = models.TimeField(null=True)

#     def __str__(self):
#         return self.Time_Out
