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
from oddrin.views import (
    OddrinViewSet,
    IdmcViewSet,
    InformRiskViewSet,
    IdmcSuddenOnsetViewSet,
    InformRiskSeasonalViewSet,
    DisplacementViewSet,
    GarHazardViewSet,
    PdcDisplacementViewSet
)
from ipc.views import (
    GlobalDisplacementViewSet,
    ThinkHazardInformationViewSet
)

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'earthquake', EarthquakeViewSet, basename='earthquake')
router.register(r'global-exposure-data', OddrinViewSet, basename='oddrin')
router.register(r'idmc-data', IdmcViewSet, basename='idmc')
router.register(r'displacement-data', GlobalDisplacementViewSet, basename='global')
router.register(r'inform-data', InformRiskViewSet, basename='inform')
router.register(r'idmc-return-period-data', IdmcSuddenOnsetViewSet, basename='idmc return period')
router.register(r'inform-seasonal-data', InformRiskSeasonalViewSet, basename='inform seasonal')
router.register(r'exposure-data', DisplacementViewSet, basename='global exposure')
router.register(r'hazard_info', ThinkHazardInformationViewSet, basename='hazard info')
router.register(r'gar-return-period', GarHazardViewSet, basename='gar return period')
router.register(r'pdc-displacement', PdcDisplacementViewSet, basename='pdc displacement')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
