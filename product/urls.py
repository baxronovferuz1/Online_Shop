from rest_framework.routers import SimpleRouter
from .views import ShowTelevisions
from django.urls import path, include


router=SimpleRouter()

router.register("TV", ShowTelevisions, basename="tv")



urlpatterns = [
    path('', include(router.urls)),
]
