from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# Here We Will Create Models.
# Remeber make makemigration will always save the changes in a folder named migrations it is not saved untill we migrate it
# Whatever change you will do here to save that changes in your database you should migrate that
# pyhon manage.py makemigrations is used to save changes while migrate is used to commit them in database
# here database is in our admin pannel where in the product section we get all these fields and from there we can add product
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)#if no price is given then automatically set default price to 0
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
# In image field here default is neccesary because the image that you didnt uploaded should have some default value
# Changing the below function not require migration because we are not changing the model we are here changing the function only
# This function is used so that in place of product object1 and productobject2 in admin pannel it will display product name in admin panel
    def __str__(self):
        return self.product_name


class CartItem(models.Model):
    customer_name = models.CharField(max_length=40)
    item_quantity = models.IntegerField(default=1)
    product_detail = models.ForeignKey(Product , null=True , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_detail.product_name

class OrderedProduct(models.Model):
    customer_name = models.CharField(max_length=40)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile_no = PhoneNumberField()
    dilevery_mode = models.CharField(max_length=30)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

    def _str_(self):
        return self.product.product_name
