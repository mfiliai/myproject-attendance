# Generated by Django 3.0.6 on 2020-07-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancemof', '0002_treasury_purposes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stafflist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]