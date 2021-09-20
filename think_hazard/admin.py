from django.contrib import admin

from think_hazard.models import ThinkHazardCountry


@admin.register(ThinkHazardCountry)
class ThinkHazardCountryAdmin(admin.ModelAdmin):
    pass
