from django.contrib import admin

from think_hazard.models import (
    ThinkHazardCountry,
    HazardDetail,
    Hazard
)


@admin.register(ThinkHazardCountry)
class ThinkHazardCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(HazardDetail)
class HazardDetailAdmin(admin.ModelAdmin):
   pass


@admin.register(Hazard)
class HazardAdmin(admin.ModelAdmin):
    pass
