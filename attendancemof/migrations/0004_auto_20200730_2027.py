# Generated by Django 3.0.6 on 2020-07-30 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("attendancemof", "0003_auto_20200730_1814"),
    ]

    operations = [
        migrations.RenameField(model_name="stafflist", old_name="id", new_name="Code",),
    ]
