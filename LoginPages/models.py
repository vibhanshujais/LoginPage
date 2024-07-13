from django.db import models

""" class SignUpData(models.Model):
    full_name = models.TextField()
    username = models.TextField()
    contact = models.PositiveBigIntegerField()
    email_id = models.EmailField()
    password = models.TextField() """

class signupdata(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.TextField()
    contact = models.PositiveBigIntegerField()
    email_id = models.EmailField(max_length=255,unique=True)
    password = models.TextField()