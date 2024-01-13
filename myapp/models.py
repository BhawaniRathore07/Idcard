from django.db import models


class Pak_IdCard(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='idcards')


class Template(models.Model):
    template=models.ImageField(upload_to='templates')


class Balaji_IdCard(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    course=models.CharField(max_length=10)
    dob=models.CharField(max_length=40)
    address=models.CharField(max_length=300)
    state=models.CharField(max_length=40)
    image=models.ImageField(upload_to='idcards')
    mobile=models.IntegerField(max_length=10)