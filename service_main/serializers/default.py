from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ModelField, SerializerMethodField
from service_main.models import Category, CategoryDetail, Product, Geography, Province, Amphur, \
    District, Choice, Profile, Farm, Social, Map
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','first_name','last_name']

class GeographySerializer(ModelSerializer):
    class Meta:
        model = Geography
        fields = '__all__'

class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class AmphurSerializer(ModelSerializer):
    class Meta:
        model = Amphur
        fields = '__all__'

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(ModelSerializer):

    class Meta:
        model = CategoryDetail
        fields = '__all__'

class CategoryFullSerializer(ModelSerializer):
    detail = SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
    def get_detail(self,obj):
        data = CategoryDetail.objects.filter(category=obj.id)
        response = CategoryDetailSerializer(data, many=True)
        return response.data




class ProductFileSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['file1','file2','file3','file4','file5']


class ProductSerializer(ModelSerializer):
    categories = SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
    def get_categories(self,obj):
        category = CategoryFullSerializer(obj.category, many=True)
        return category.data

class FarmFullSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    province = ProvinceSerializer(read_only=True)
    amphur = AmphurSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    user_image = SerializerMethodField(read_only=True)
    class Meta:
        model = Farm
        fields = '__all__'
    def get_user_image(self,obj):
        user = obj.user.id
        try:
            profile = Profile.objects.get(user=user)
            profile = ProfileFullSerializer(profile)
            return profile.data["profile_image"]
        except:
            return None




class ProductFullSerializer(ModelSerializer):
    category = CategoryDetailSerializer(read_only=True, many=True)
    farm = FarmFullSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'




class GeographySerializer(ModelSerializer):

    class Meta:
        model = Geography
        fields = '__all__'


class ProvinceSerializer(ModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'


class AmphurSerializer(ModelSerializer):

    class Meta:
        model = Amphur
        fields = '__all__'


class DistrictSerializer(ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    # labels = SerializerMethodField()
    class Meta:
        model = Profile
        exclude = ['profile_image','presonal_image']

class ProfileFullSerializer(ModelSerializer):
    # labels = SerializerMethodField()
    geo = GeographySerializer()
    province = ProvinceSerializer()
    amphur = AmphurSerializer()
    district = DistrictSerializer()
    province = ProvinceSerializer()
    class Meta:
        model = Profile
        fields = '__all__'


class FarmSerializer(ModelSerializer):

    class Meta:
        model = Farm
        fields = '__all__'


class SocialSerializer(ModelSerializer):

    class Meta:
        model = Social
        fields = '__all__'


class ProfileImageSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_image', 'id', 'user',)


class PersonalImageSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('presonal_image', 'id', 'user',)

class UserEditSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','id','is_staff','is_superuser','is_active')

class MapSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
