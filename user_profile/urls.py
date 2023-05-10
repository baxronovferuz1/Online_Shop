from django.urls import path , include


from rest_framework.routers import DefaultRouter

from user_profile.views import *

router = DefaultRouter()
router.register("update_profile" , UpdateProfileView , basename = 'userprofile')
router.register("shopping_cart", ShowMyShoppingCartView, basename="myshopping_cart")


urlpatterns=[
    path("signup/", UserSignUPAPIView.as_view()),
    path("edit_profile", include(router.urls)),
]