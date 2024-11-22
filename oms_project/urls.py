"""
URL configuration for oms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

scheme_view = get_schema_view(
    openapi.Info(
        title='Lead managment client form API',
        default_version='Version 1',
        description='Endpoint for client form data',
        terms_of_service='',
        contact=openapi.Contact(email='liuyuenfu@gmail.com'),
        license=openapi.License(name='D191t8l9h0x7')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('account/', include('account.urls')),
    path('lead-management/', include('lead_management_app.urls')),
    path('lead-management-serializer/', include('lead_management_serializer.urls')),
    path('forms/', include('forms_app.urls')),
    path("schema", scheme_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path("docs", scheme_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
