# Generated by Django 3.0.7 on 2020-08-10 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200809_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='Date',
        ),
    ]
