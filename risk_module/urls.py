"""risk_module URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include, static
from django.urls import path
from django.conf import settings

from earthquake.views import EarthquakeViewSet
from think_hazard.views import HazardViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'earthquake', EarthquakeViewSet, basename='earthquake')
router.register(r'think-hazard', HazardViewSet, basename='think hazard')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
