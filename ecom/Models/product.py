from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

OPTIONS = {
    ('Park','Park'),
    ('Hotel','Hotel'),
    ('School','School'),
    ('Resturant','Resturant'),
    ('Other','Other'),
}

class Product(BaseModel):
    code =models.IntegerField()
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    for_what = models.CharField(
        choices=OPTIONS,
        max_length=100,
        default='Other'
    )
    product_img = models.ImageField(
        upload_to='image/',
        null=True,
        max_length=255
    )
    Description = models.TextField()

    def __str__(self):
        return f"{self.product_name} {self.price}"

    def image_tag(self):
        return mark_safe(
            '<img src="http://127.0.0.1:8000/media/%s" width="150" height="150"/>' %
            (self.product_img)
        )
    image_tag.allow_tags = True

class ContactUs(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"