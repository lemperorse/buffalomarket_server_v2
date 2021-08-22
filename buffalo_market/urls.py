"""buffalo_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django_restful_admin import admin as api_admin
from django.conf.urls.static import static
from django.conf import settings
from revproxy.views import ProxyView
from django.conf.urls import url
from django.shortcuts import redirect

admin.site.site_header = 'ระบบหลังบ้าน ตลาดควาย'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('apiadmin/', api_admin.site.urls),
    path('api/default/', include('service_core.urls.default')),
    path('api/user/', include('service_core.urls.user')),
    path('api/admin/', include('service_core.urls.admin')),
    path('api/', include('service_core.urls.guest')),
    url(r'^buffalo_market_typescript/(?P<path>.*)$' , ProxyView.as_view(upstream='https://lemperorse.github.io/buffalo_market_typescript/') ),
     path('', lambda request: redirect('buffalo_market_typescript/', permanent=True)),
]
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
