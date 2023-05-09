from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import Factor

router = DefaultRouter()
router.register('Factors', Factor, basename ='factor')

urlpatterns=[
    path('suppliar/', include(router.urls)),
]