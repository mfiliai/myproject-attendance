from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dash, name="dashboard"),
    path("stafflist/", views.stafflist, name="stafflist"),
    # path("createStaff/", views.createStaff, name="createStaff"),
    # path("updateStaff/<str:pk>/", views.updateStaff, name="updateStaff"),
    # path("deleteStaff/<str:pk>/", views.deleteStaff, name="deleteStaff"),
    path("attendances/", views.attendance_list, name="attendances"),
    path("manageAttendance/", views.manage_attendance, name="manageAttendance"),
    # path("updateAttendance/<str:pk>/", views.updateAttendance, name="updateAttendance"),
    # path("deleteAttendance/<str:pk>/", views.deleteAttendance, name="deleteAttendance"),
    # path("deduction/", views.deduction, name="deduction"),
    # path("createDeduction/", views.createDeduction, name="createDeduction"),
    # path("updateDeduction/<str:pk>/", views.updateDeduction, name="updateDeduction"),
    # path("deleteDeduction/<str:pk>/", views.deleteDeduction, name="deleteDeduction"),
]
