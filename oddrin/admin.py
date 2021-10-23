from django.contrib import admin

from oddrin.models import Oddrin


@admin.register(Oddrin)
class OddrinAdmin(admin.ModelAdmin):
    pass
