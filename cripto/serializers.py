from rest_framework import serializers
from .models import Self


class SelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Self
        fields = ("public_key",)
