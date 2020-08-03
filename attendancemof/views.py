# Stafflist.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Login Restrictions
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

# LOGIN
@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dash")
        else:
            messages.info(request, "Username of Password is incorrect")

    context = {}
    return render(request, "attendancemof/loginPage.html", context)


def logoutUser(request):
    logout(request)
    return redirect("/loginPage")


@login_required(login_url="loginPage")
@allowed_users(allowed_roles=["admin", "Staff"])


# HOME.
def dash(request):

    return render(request, "attendancemof/dashboard.html")

    # Division= Stafflist.objects
    # divisions_count= Stafflist.objects.filter(Division=Division).count()
    # late_count= AttendanceT20.objects.filter(Attendance=Late).count()


# STAFFLIST__________________
@login_required(login_url="loginPage")
def stafflist(request):
    stafflists = Stafflist.objects.all()
    return render(request, "attendancemof/stafflist.html", {"stafflists": stafflists})


@login_required(login_url="loginPage")
def createStaff(request):
    form = StaffForm()
    if request.method == "POST":
        # print('Printing POST:', request.POST)
        form = StaffForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/stafflist")
    context = {"form": form}
    return render(request, "attendancemof/createStaff.html", context)


@login_required(login_url="loginPage")
def updateStaff(request, pk):
    staffs = Stafflist.objects.get(Code=pk)
    form = StaffForm(instance=staffs)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=staffs)
    if form.is_valid():
        form.save()
        return redirect("/stafflist")
    context = {"form": form}
    return render(request, "attendancemof/createStaff.html", context)


@login_required(login_url="loginPage")
def deleteStaff(request, pk):
    staffs = Stafflist.objects.get(Code=pk)
    if request.method == "POST":
        staffs.delete()
        return redirect("/stafflist")

    context = {"item": staffs}
    return render(request, "attendancemof/delete.html", context)


# ATTENDANCE___________
@login_required(login_url="loginPage")
def attendance(request):
    attendances = AttendanceT20.objects.all()
    return render(
        request, "attendancemof/attendance.html", {"attendances": attendances}
    )


@login_required(login_url="loginPage")
def takeAttendance(request):
    form = AttendanceForm()
    if request.method == "POST":
        # print('Printing POST:', request.POST)
        form = AttendanceForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/attendance")
    context = {"form": form}
    return render(request, "attendancemof/takeAttendance.html", context)


@login_required(login_url="loginPage")
def updateAttendance(request, pk):
    attendees = AttendanceT20.objects.get(a_id=pk)
    form = AttendanceForm(instance=attendees)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendees)
    if form.is_valid():
        form.save()
        return redirect("/attendance")
    context = {"form": form}
    return render(request, "attendancemof/updateAttendance.html", context)


@login_required(login_url="loginPage")
def deleteAttendance(request, pk):
    attendees = AttendanceT20.objects.get(a_id=pk)
    if request.method == "POST":
        attendees.delete()
        return redirect("/attendance")

    context = {"item": attendees}
    return render(request, "attendancemof/deleteAttendance.html", context)


# DEDUCTIONS___________
@login_required(login_url="loginPage")
def deduction(request):
    deductions = TreasuryPurposes.objects.all()
    return render(request, "attendancemof/deduction.html", {"deductions": deductions})


@login_required(login_url="loginPage")
def createDeduction(request):
    form = DeductionForm()
    if request.method == "POST":
        # print('Printing POST:', request.POST)
        form = DeductionForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/deduction")
    context = {"form": form}
    return render(request, "attendancemof/createDeduction.html", context)


@login_required(login_url="loginPage")
def updateDeduction(request, pk):
    deductions = TreasuryPurposes.objects.get(t_id=pk)
    form = DeductionForm(instance=deductions)
    if request.method == "POST":
        form = DeductionForm(request.POST, instance=deductions)
    if form.is_valid():
        form.save()
        return redirect("/deduction")
    context = {"form": form}
    return render(request, "attendancemof/createDeduction.html", context)


@login_required(login_url="loginPage")
def deleteDeduction(request, pk):
    deductions = TreasuryPurposes.objects.get(t_id=pk)
    if request.method == "POST":
        deductions.delete()
        return redirect("/deduction")

    context = {"item": deductions}
    return render(request, "attendancemof/deleteDeduction.html", context)
