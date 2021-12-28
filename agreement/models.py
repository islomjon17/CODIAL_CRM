from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class course(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.IntegerField()

    def __str__(self):
        return self.nom

status_choices = [('new', 'new'),('loyal', 'loyal'),]

class student(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    sharif = models.CharField(max_length=50)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    telifon1 = PhoneNumberField(null=False, blank=False, unique=True)
    telifon1 = PhoneNumberField(null=False, blank=True, unique=True)
    status = models.CharField(max_length=15 , choices=status_choices)

    def __str__(self):
        return self.ism

class teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)



class agreement(models.Model):
    kurs_vaqtlari =  (
        ("08:00-10:00", "08:00-10:00"),
        ("10:00-12:00", "10:00-12:00"),
        ("14:00-16:00", "14:00-16:00"),
        ("16:00-18:00", "16:00-18:00"),
        ("18:00-20:00", "18:00-20:00"),
    )
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(course,  on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(student,  on_delete=models.SET_NULL, null=True)
    shartnoma_raqammi = models.integerField()
    kunlari = models.CharField(max_length=30, choices=(("Dushanba-Juma","Dushanba-Juma"),("Sheshanba-Shanba","Sheshanba-Shanba")))
    kurs_vaqti = models.CharField(max_length=50, choices=kurs_vaqtlari)
    guruh_nomi = models.CharField(max_length=50)
    tuzuvchi = models.CharField(max_length=50)
    sinov_darsi_anasi = models.DateField()
    status = models.CharField(max_length=50, choices=(("Activa", "Activa"),("Passive", "Passive")))

    def __str__(self):
        return f"#{self.shartnoma_raqammi},{self.student}, {self.shartnoma}"



