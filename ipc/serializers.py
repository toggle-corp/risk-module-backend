from rest_framework import serializers

from ipc.models import Ipc


class IpcSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ipc
        fields = '__all__'
