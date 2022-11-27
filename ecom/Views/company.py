from ..serializers.company import CompanySerializers, CompanyOwnerSerializers
from ..Models.company import Company, CompanyOwner
from rest_framework import viewsets


class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class  = CompanySerializers

class CompanyOwnerViewset(viewsets.ModelViewSet):
    queryset = CompanyOwner.objects.all()
    serializer_class = CompanyOwnerSerializers()