from django.urls import path , include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from user_profile.views import *

router = DefaultRouter()
router.register("update_profile" , UpdateProfileView , basename = 'userprofile')
router.register("shopping_cart", ShowMyShoppingCartView, basename="myshopping_cart")


urlpatterns=[
    path("signup/", UserSignUPAPIView.as_view()),
    path("edit_profile", include(router.urls)),
    path("edit_profile/token/",TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("edit_profile/token/refresh/",TokenRefreshView.as_view(), name="token-refresh"),
]