from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Factor

router=DefaultRouter

router.register("Factor", Factor, basename="Factor" )


urlpatterns=[
    path("suppliar/", include(router.urls))
]