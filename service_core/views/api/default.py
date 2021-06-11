from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend, BaseInFilter, NumberFilter
from rest_framework.viewsets import ModelViewSet
from service_main.serializers.default import CategorySerializer, CategoryDetailSerializer, \
    ProductSerializer, GeographySerializer, ProvinceSerializer, AmphurSerializer, DistrictSerializer, ChoiceSerializer, \
    ProfileSerializer, FarmSerializer, SocialSerializer, ProfileFullSerializer, CategoryFullSerializer, \
    ProductFullSerializer, MapSerializer, ProductFileSerializer
from service_main.models import Category, CategoryDetail, Product, Geography, Province, Amphur, \
    District, Choice, Profile, Farm, Social, Map
from rest_framework import generics,filters

from service_main.services.filter import ProductFilter


class MapViewSet(ModelViewSet):
    queryset = Map.objects.order_by('pk')
    serializer_class = MapSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer


class CategoryDetailViewSet(ModelViewSet):
    queryset = CategoryDetail.objects.order_by('pk')
    serializer_class = CategoryDetailSerializer

class CategoryFullViewSet(ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategoryFullSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name',]



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ProductFilter
    search_fields = ['name','farm__name','category__name','category__category__name','status']

class ProductFileViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductFileSerializer

class ProductFullViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductFullSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ProductFilter
    search_fields = ['name','price','price_start','price_end']

class GeographyViewSet(ModelViewSet):
    queryset = Geography.objects.order_by('pk')
    serializer_class = GeographySerializer


class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.order_by('pk')
    serializer_class = ProvinceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['geo', ]


class AmphurViewSet(ModelViewSet):
    queryset = Amphur.objects.order_by('pk')
    serializer_class = AmphurSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['province', ]


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.order_by('pk')
    serializer_class = DistrictSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['province', 'amphur']


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.order_by('pk')
    serializer_class = ChoiceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', 'value']


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user','personal_id','tel']

class ProfileFullViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileFullSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user',]

class FarmViewSet(ModelViewSet):
    queryset = Farm.objects.order_by('pk')
    serializer_class = FarmSerializer

class FarmUserViewSet(ModelViewSet):
    queryset = Farm.objects.order_by('pk')
    serializer_class = FarmSerializer

class SocialViewSet(ModelViewSet):
    queryset = Social.objects.order_by('pk')
    serializer_class = SocialSerializer
