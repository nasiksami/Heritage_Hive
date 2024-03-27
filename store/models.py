from django.db import models
from Category.models import Category
from  django.urls import reverse
from account.models import Account
# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=500)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    price=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE,blank=True,null=True)

    def get_url(self):
        return reverse('product_details',args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name


variation_category_choice = (
    ('color','color'),
    ('size','size'),
)


class Variationmanager(models.Manager):
    def colors(self):
        return super(Variationmanager,self).filter(variation_category='color',is_active=True)
    def sizes(self):
        return super(Variationmanager,self).filter(variation_category='size',is_active=True)    
        
              
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice) 
    variation_value=models.CharField(max_length=100,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    objects=Variationmanager()



    def __str__(self):
        return str(self.variation_value)


class ReviewRating(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,blank=True)
    review=models.TextField(max_length=500,blank=True)
    rating=models.FloatField()
    ip=models.CharField(max_length=20,blank=True)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)





    def __str__(self):
        return self.subject






        
