from django.contrib import admin

from ipc.models import Ipc


@admin.register(Ipc)
class IpcAdmin(admin.ModelAdmin):
    pass
