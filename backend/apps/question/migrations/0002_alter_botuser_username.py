# Generated by Django 5.0.2 on 2024-02-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
