from django.contrib import admin

from think_hazard.models import (
    ThinkHazardCountry,
    HazardInformation,
    Hazard
)


@admin.register(ThinkHazardCountry)
class ThinkHazardCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(HazardInformation)
class HazardDetailAdmin(admin.ModelAdmin):
   pass


@admin.register(Hazard)
class HazardAdmin(admin.ModelAdmin):
    pass
