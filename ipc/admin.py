from django.contrib import admin

from ipc.models import Ipc, Country, GlobalDisplacement


@admin.register(Ipc)
class IpcAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(GlobalDisplacement)
class GlobalDisplacement(admin.ModelAdmin):
    pass
