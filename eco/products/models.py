from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload="categories")

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey()