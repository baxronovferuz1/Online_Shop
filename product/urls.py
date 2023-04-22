from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path, include


router=SimpleRouter()

router.register("TV", ShowTelevisions, basename="tv")
router.register("Book", ShowBook, basename="book")
router.register("Computer", ShowComputer, basename="computer")
router.register("Mobile", ShowMobile, basename="mobile")
router.register("Stationery", ShowStationery, basename="stationery")




urlpatterns = [
    path('', include(router.urls)),
]
