from django.db import models
from datetime import datetime 


# Create your models here.
class contact_table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122,default=' ')
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    decs = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name


class order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=122)
    product_price = models.CharField(max_length=122)
    quantity = models.CharField(max_length=122)
    user_id = models.CharField(max_length=122,default= ' ')
    user_name = models.CharField(max_length=122,default= ' ')
    product_id = models.CharField(max_length=122,default= ' ')
    date = models.DateField(default=datetime.now)


    def __str__(self):
        return self.product_name

    
class Add_product(models.Model):
    name = models.CharField(max_length=122)
    img = models.FileField(upload_to="uploads/")
    price = models.FloatField()    

    def __str__(self):
        return self.name

