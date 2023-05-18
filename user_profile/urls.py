from django.urls import path , include
from rest_framework_simplejwt.views import ob
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from rest_framework.routers import DefaultRouter
# from rest_framework_simplejw

from user_profile.views import *

router = DefaultRouter()
router.register("update_profile" , UpdateProfileView , basename = 'userprofile')
router.register("shopping_cart", ShowMyShoppingCartView, basename="myshopping_cart")


urlpatterns=[
    path("signup/", UserSignUPAPIView.as_view()),
    path("login/", obtain_jwt_token),
    path("edit_profile", include(router.urls)),
    path("api-refresh-token/", refresh_jwt_token),
]