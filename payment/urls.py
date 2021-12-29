from .views import *
from django.urls import path, include
urlpatterns = [
    path('payment', PaymentListCreateView.as_view(), 'payment'),
    path('payment/<int:pk>', PaymentListUpdateAPIView.as_view(), 'paymentupdate')
]