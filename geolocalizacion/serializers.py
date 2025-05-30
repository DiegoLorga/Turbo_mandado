# Estamos definiendo los serializadores para las entidades de geolocalización.
from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields = __all__  # Serializa todos los campos del modelo Location