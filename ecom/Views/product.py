from ..serializers.product import ProductSerializers, ContactUsSerializers
from ..Models.product import Product, ContactUs
from rest_framework import viewsets

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def destroy(self, request):
        raise self.permission_denied(
            request,
            message="you do not have permission to delete product"
        )

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    def destroy(self, request, pk):
        raise self.permission_denied(
            request,
            message="you do not have permission to do this action"
        )
