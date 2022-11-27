from ..Models.product import Product, ContactUs
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate(self, attrs):
        if self.context.get('request').method != 'GET':
            raise serializers.ValidationError({
                'error':'you do not have permission to do this action'
            })
        return attrs

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

