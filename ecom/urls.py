from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .Views.product import ProductViewset, ContactUsViewset
from .Views.company import CompanyOwnerViewset ,CompanyViewset
router = DefaultRouter()
router.register(r'product',ProductViewset,basename='product')
router.register(r'contactus',ContactUsViewset,basename='contactus')
router.register(r'company', CompanyViewset,basename='company')
router.register(r'owner', CompanyOwnerViewset,basename='owner')



urlpatterns = [
    path('',include(router.urls)),
]