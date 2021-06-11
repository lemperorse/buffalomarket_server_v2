from django.urls import path,include
from rest_framework.schemas import get_schema_view 
from service_core.views.user.UserCreate import Register
from service_core.views.api import default as views
from service_core.views.user import  UserCreate
from service_core.views.user import  Product
urlpatterns = [
    path('test',views.CategoryViewSet.as_view({'get': 'list'})),
    path('test2',UserCreate.CategoryAPIListView.as_view()),
    path('product',Product.ProductView.as_view()),
    path('personal/image/<int:id>/', UserCreate.ImagePersonal.as_view()),
    path('profile/image/<int:id>/', UserCreate.ImageProfile.as_view()),
    path('password/<int:id>/', UserCreate.ManageUser.as_view()),
    path('farm/<int:id>/', UserCreate.FarmUserAPIView.as_view()),
]