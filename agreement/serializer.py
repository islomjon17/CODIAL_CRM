from rest_framework.serializers import serializers
from .models import *

class KursiSerializer(serializers.ModelSerializerFactory):
    class Meta:
        models = course
        fields = ('nom', 'narx')

class StudentVaqtlariSerializer(serializers.ModelSerializerFactory):
    class Meta:
        models = student
        fields = ('ism', 'familya', 'sharif', 'gender', 'telifon1', 'telifon2', 'status')

class TeacherVaqtlariSerializer(serializers.ModelSerializerFactory):
    class Meta:
        models = teacher
        fields = ('name', 'age', 'phone')

class AgreementVaqtlariSerializer(serializers.ModelSerializerFactory):
    class Meta:
        models = agreement
        fields = ('teacher', 'course', 'student', 'shartnoma_raqami',
        'kunlari', 'kurs_vaqti','guruh_nomi', 'tuzuvchi',
        'sinov_darsi_anasi', 'status')