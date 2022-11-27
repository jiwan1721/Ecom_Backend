from django.db import models
from .product import BaseModel


class CompanyOwner(BaseModel):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(
        max_length=50,
        null=True
    )
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=100)
    provience = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.middle_name + " " + self.last_name
    
    def full_name(self):
        if self.middle_name:
            return "{self.first_name} {self.middle_name} {self.last_name}"
        return "{self.first_name} {self.last_name}"
    def address(self):
        return f"{self.city},{self.district},{self.country}"



class Company(BaseModel):
    company_name = models.CharField(max_length=200)
    company_phone_number = models.IntegerField
    company_location = models.CharField(max_length=200)
    owner = models.ForeignKey(
        CompanyOwner,
        related_name='owner',
        on_delete=models.CASCADE
    )
    country = models.CharField(max_length=100)
    provience = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    def __str__(self) -> str:
        return "Company name: %s, Phone no: %s" % (
            self.company_name,
            self.company_phone_number,
        )

