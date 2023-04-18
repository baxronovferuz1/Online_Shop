from django.urls import path , include


from rest_framework.routers import DefaultRouter

from user_profile import views

router = DefaultRouter()
router.register('update_profile' , views.UpdateProfileView , basename = 'userprofile')

urlpatterns={
    path("signup/", views.UserSignUPAPIView.as_view())
}