from django.contrib import admin

from oddrin.models import Oddrin, Idmc, InformRisk


@admin.register(Oddrin)
class OddrinAdmin(admin.ModelAdmin):
    pass


@admin.register(Idmc)
class IdmcAdmin(admin.ModelAdmin):
    pass


@admin.register(InformRisk)
class InformRiskAdmin(admin.ModelAdmin):
    pass
