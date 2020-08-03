# Generated by Django 3.0.6 on 2020-07-30 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("attendancemof", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="treasury_purposes",
            fields=[
                (
                    "attendancet20_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="attendancemof.AttendanceT20",
                    ),
                ),
                ("Time_Out", models.DateTimeField(null=True)),
                ("Late_hours", models.DateTimeField(null=True)),
                ("Overtime_In", models.DateTimeField(null=True)),
                ("Overtime_Out", models.DateTimeField(null=True)),
                ("Deduction_Hours", models.DateTimeField(null=True)),
            ],
            bases=("attendancemof.attendancet20",),
        ),
    ]
