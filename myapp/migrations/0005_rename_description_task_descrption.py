# Generated by Django 4.2.4 on 2023-08-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_descrption_task_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='descrption',
        ),
    ]