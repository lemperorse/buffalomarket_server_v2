from django.urls import path,include
from rest_framework.schemas import get_schema_view
from service_core.views.user.UserCreate import Register

urlpatterns = [
  path('auth/', include('rest_auth.urls'), name="login"),
  path('register/', Register.as_view(),name="Register"),

] 