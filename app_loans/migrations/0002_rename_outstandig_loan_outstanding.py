# Generated by Django 3.2.23 on 2024-01-22 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='outstandig',
            new_name='outstanding',
        ),
    ]