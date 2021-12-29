from django.shortcuts import render
from agreement.serializer import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# Create your views here.
class KursVaqtiView(generics.ListCreateAPIView):
    queryset = course.objects.all()
    serializer_class = KursiSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = KursiSerializer(queryset, many=True)
        return Response(serializer.data)