from rest_framework import serializers


from .models import *

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models = payment
        fields = ('agreement', 'teacher', 'course', 'student'
        , 'payment_year'
        , 'payment_month'
        , 'discount_status'
        , 'discount_reason'
        , 'discount_size'
        , 'payment_date'
        , 'must_pay'
        , 'cashier'
        , 'in_hand'
        , 'bank'
        , 'card'
        , 'payed'
        , 'rest_money')
        