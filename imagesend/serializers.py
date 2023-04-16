from rest_framework import serializers
from .models import SendImage

# Serializer for UploadAlert Model
class SendImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendImage
        fields = ('pk','image','text')