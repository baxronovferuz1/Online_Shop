
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Online Shop',
        default_version='v1',
        description='Online_shopping',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# urlpatterns=[
#     path('i18n/', include('django.conf.urls.i18n')),
# ]




# urlpatterns+=i18n_patterns(
urlpatterns=[   
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')),
    path('', include('product.urls')),
    path('', include('Shopping_Cart.urls')),
    path('', include('suppliar.urls')),
    path(
        "docs/", schema_view.with_ui("swagger", cache_timeout=0), name="docs"
    ),
    path(
        "docs2/", schema_view.with_ui("redoc", cache_timeout=0), name="docs2"
    ),
    
 ]