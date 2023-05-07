from django.urls import path,include

from .views import My_Cart,Payment,My_Orders
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("my_cart", My_Cart, basename="My_Cart")
router.register("my_orders", My_Orders, basename="My_Orders")
router.register("payment", Payment, basename="Payment")

urlpattern={
    path("", include(router.urls)),
}