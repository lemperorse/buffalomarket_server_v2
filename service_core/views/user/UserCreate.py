from django.contrib.auth.models import User

from service_main.serializers.default import PersonalImageSerializer, ProfileImageSerializer, UserEditSerializer, \
    FarmSerializer
from service_main.serializers.register import UserCreateSerializer
from service_main.models import Choice, Profile, Farm
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_vueformgenerator.schema import Schema
from django import forms
from django.forms.models import modelform_factory,modelformset_factory,inlineformset_factory
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import base64
import uuid
import json

def convertImagetofile(img):
    format, imgstr = img.split(';base64,')
    ext = format.split('/')[-1]
    image_name = str(uuid.uuid4()) + "."+ext
    return ContentFile(base64.b64decode(imgstr), image_name)

class ImagePersonal(APIView):
    def get(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
            serializer = PersonalImageSerializer(item,context={"request": request})
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        request.data['presonal_image'] = convertImagetofile(request.data.get('presonal_image'))
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        serializer = PersonalImageSerializer(item, data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ImageProfile(APIView):
    def get(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
            serializer = ProfileImageSerializer(item,context={"request": request})
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        request.data['profile_image'] = convertImagetofile(request.data.get('profile_image'))
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        serializer = ProfileImageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ManageUser(APIView):
    def delete(self, request, id, format=None):
        try:
            user = User.objects.get(pk=id)
            user.is_active = False
            user.save()
            serializer = UserEditSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def post(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
            item.status = request.data['status']
            item.save()
            serializer = ProfileSerializer(item)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            user = User.objects.get(pk=id)
            user.set_password(request.data['password'])
            user.save()
            serializer = UserEditSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)


class FarmUserAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Farm.objects.get(user=id)
            serializer = FarmSerializer(item)
            return Response(serializer.data)
        except Farm.DoesNotExist:
            return Response(status=404)


class TestForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=128)

class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = []

from django.db import connection
class CategoryAPIListView(APIView):
    def get(self, request, format=None):
        lname = ""
        c = connection.cursor()
        c.execute("SELECT * FROM buffaloservice_choice")
        rows = c.fetchall()
        return Response(rows)



