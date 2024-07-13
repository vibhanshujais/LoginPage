# Generated by Django 5.0.7 on 2024-07-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupdata',
            name='email_id',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='signupdata',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]