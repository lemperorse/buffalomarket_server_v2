from django.contrib.auth.models import User
from service_main.serializers.default import PersonalImageSerializer, ProfileImageSerializer, UserEditSerializer, \
    FarmSerializer, ProductFullSerializer
from service_main.serializers.register import UserCreateSerializer
from service_main.models import Choice, Profile, Farm, Product
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

class ProductView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        response = ProductFullSerializer(product,many=True)
        return Response(response.data)