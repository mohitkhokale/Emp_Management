# Generated by Django 4.0.3 on 2022-03-10 10:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0023_alter_task_date_of_submit_remove_task_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_submit',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 15, 45, 16, 650287)),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]