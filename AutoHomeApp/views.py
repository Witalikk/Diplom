from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from AutoHomeApp.models import *
from AutoHomeApp.serializers import *


# Create your views here.

class Logout(APIView):

    @staticmethod
    def get(request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUserSerializers
    lookup_field = 'pk'


class MarkasListView(generics.ListAPIView):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializers


class ModelAutoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = UpdateModelAutoSerializers


class UpdateSMSListView(generics.RetrieveUpdateAPIView):
    queryset = SMS.objects.all()
    serializer_class = UpdateSMSAutoSerializers


class ModelAutoDestroyView(generics.DestroyAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = CreateModelAutoSerializers


class ModelAutoRetrieveView(generics.RetrieveAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = ModelAutoSerializers


class ModelAutoCreateView(generics.CreateAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = CreateModelAutoSerializers


class ModelAutoListView(generics.ListAPIView):
    serializer_class = ModelAutoSerializers

    def get_queryset(self):
        queryset = ModelAuto.objects.all()

        params = self.request.query_params

        model = params.get('model', None)
        body_type = params.get('body_type', None)
        min_price = params.get('min_price', None)
        max_price = params.get('max_price', None)

        if model:
            queryset = queryset.filter(model=model)

        if body_type:
            queryset = queryset.filter(body_type=body_type)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class SoldCarListView(generics.ListAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = SoldCarsSerializers


class SoldCarCreateView(generics.CreateAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = CreateSoldCarsSerializers


class SoldCarDestroyView(generics.DestroyAPIView):
    queryset = SoldCars.objects.all()
    serializer_class = CreateSoldCarsSerializers


class InquiryListView(generics.ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializers


class InquiryCreateView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = CreateInquirySerializers


class InquiryDestroyView(generics.DestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = CreateInquirySerializers


class TestDriveListView(generics.ListAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializers


class TestDriveCreateView(generics.CreateAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = CreateTestDriveSerializers


class TestDriveDestroyView(generics.DestroyAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = CreateTestDriveSerializers


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializers


class ServiceDestroyView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializers


class RoomCreateView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class RoomDestroyView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDeleteSerializers


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializers


class SmsDestroyView(generics.DestroyAPIView):
    queryset = SMS.objects.all()
    serializer_class = SmsDeleteSerializers


class SMSCreateView(generics.CreateAPIView):
    queryset = SMS.objects.all()
    serializer_class = CreateSMSSerializers


class SMSListView(generics.ListAPIView):
    serializer_class = SMSSerializers

    def get_queryset(self):
        queryset = SMS.objects.all()

        params = self.request.query_params

        room = params.get('room', None)

        if room:
            queryset = queryset.filter(room=room)

        return queryset
