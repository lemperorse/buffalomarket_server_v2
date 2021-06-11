from rest_framework.routers import SimpleRouter
from service_core.views.api import default as views


router = SimpleRouter()
router.register(r'map', views.MapViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'categories', views.CategoryFullViewSet)
router.register(r'categorydetail', views.CategoryDetailViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'productfile', views.ProductFileViewSet)
router.register(r'products', views.ProductFullViewSet)
router.register(r'geography', views.GeographyViewSet)
router.register(r'province', views.ProvinceViewSet)
router.register(r'amphur', views.AmphurViewSet)
router.register(r'district', views.DistrictViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'profilefull', views.ProfileFullViewSet)
router.register(r'farm', views.FarmViewSet)
router.register(r'farmuser', views.FarmUserViewSet)
router.register(r'social', views.SocialViewSet)

urlpatterns = router.urls
