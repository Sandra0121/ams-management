from rest_framework import serializers
from manage_asset.models import Asset_auto_tracking
from manage_asset.models import nonassets


class Asset_auto_trackingSerializer(serializers.ModelSerializer):

    class Meta:
        #model = Asset_auto_tracking
        model = nonassets
        #fields = ('asset_id', 'reader_loc', 'read_at')
        fields = ('asset_id', 'reader_loc', 'read_at')

