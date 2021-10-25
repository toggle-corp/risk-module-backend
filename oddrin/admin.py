from django.contrib import admin

from oddrin.models import Oddrin, Idmc


@admin.register(Oddrin)
class OddrinAdmin(admin.ModelAdmin):
    pass


@admin.register(Idmc)
class IdmcAdmin(admin.ModelAdmin):
    pass
