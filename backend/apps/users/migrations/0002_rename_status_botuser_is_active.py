# Generated by Django 5.0.2 on 2024-02-09 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botuser',
            old_name='status',
            new_name='is_active',
        ),
    ]
