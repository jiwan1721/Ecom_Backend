from django.contrib import admin
from .Models import *
from django.contrib.auth.models import Group


# Register your models here.
admin.site.unregister(Group)

class productAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'product_name',
        'price',
        'for_what',
        'product_img',
        'Description',
        'image_tag',
    )

class compayAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'company_phone_number',
        'company_location',
        'owner',
        'district',
    )

class companyOwnerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'email',
        'phone_number',
        'district',
    )

class contactUsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'contact_number',
        'description',
    )

admin.site.register(Product, productAdmin)
admin.site.register(CompanyOwner, companyOwnerAdmin)
admin.site.register(Company, compayAdmin)
admin.site.register(ContactUs, contactUsAdmin)
