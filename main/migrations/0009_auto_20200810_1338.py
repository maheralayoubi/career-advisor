# Generated by Django 3.0.7 on 2020-08-10 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_lesson_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='student',
        ),
    ]
