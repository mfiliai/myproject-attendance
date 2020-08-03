from django.urls import path
from . import views

urlpatterns = [
    path("", views.dash, name="dash"),
    path("stafflist/", views.stafflist, name="stafflist"),
    path("createStaff/", views.createStaff, name="createStaff"),
    path("updateStaff/<str:pk>/", views.updateStaff, name="updateStaff"),
    path("deleteStaff/<str:pk>/", views.deleteStaff, name="deleteStaff"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logout"),
    path("attendance/", views.attendance, name="attendance"),
    path("takeAttendance/", views.takeAttendance, name="takeAttendance"),
    path("updateAttendance/<str:pk>/", views.updateAttendance, name="updateAttendance"),
    path("deleteAttendance/<str:pk>/", views.deleteAttendance, name="deleteAttendance"),
    path("deduction/", views.deduction, name="deduction"),
    path("createDeduction/", views.createDeduction, name="createDeduction"),
    path("updateDeduction/<str:pk>/", views.updateDeduction, name="updateDeduction"),
    path("deleteDeduction/<str:pk>/", views.deleteDeduction, name="deleteDeduction"),
]
