
from django.contrib import admin
from django.urls import path, include

#------------------------------------

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.index import index


schema_view = get_schema_view(
   openapi.Info(
      title="Delivery API",
      default_version='v1',
      description='''
        Ducementation `Redoc` view can be fond [here](/doc)
        ''',
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="umanproger@ukr.net"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


#------------------------------------
from rest_framework import routers
from market.views.category import CategoryViewSet


router = routers.DefaultRouter()

router.register('category', CategoryViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('market/', include('market.urls')),
        

    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns += {
#     +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# }

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)