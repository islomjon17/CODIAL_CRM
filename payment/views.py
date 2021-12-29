from django.shortcuts import render
from .serializer import PaymentSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
# Create your views here.


class PaymentListCreateView(ListCreateAPIView):
    queryset = payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentListUpdateAPIView(RetrieveUpdateAPIView):
    queryset = payment.objects.all()
    serializer_class = PaymentSerializer


