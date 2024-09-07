from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)
    description=models.TextField(max_length=500,blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    images_before=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    it_is_very_sold=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self): 
        return self.product_name
    

class VariationManager(models.Manager):
    def tallas(self):
        return super(VariationManager,self).filter(variation_category='talla',is_active=True)


variation_category_choice=(
    ('talla','talla'),
)
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value =models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)

    objects=VariationManager()

    def __str__(self): 
        return self.variation_category + ':'+ self.variation_value


    
    


