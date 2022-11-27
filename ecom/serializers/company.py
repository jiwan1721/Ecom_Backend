from ..Models import Company,CompanyOwner
from rest_framework import serializers

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyOwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyOwner
        fileds = '__all__'