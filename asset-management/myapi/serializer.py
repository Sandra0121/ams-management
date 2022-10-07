from rest_framework import serializers

from .models import assets




class assetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = assets
        fields = ('name')