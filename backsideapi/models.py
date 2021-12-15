from django.db import models
from django.db.models.base import Model

# # Create your models here.

# class Category(models.Model):
#     categoryid = models.AutoField(primary_key=True)
    # itemCategory = models.CharField(max_length=25)


#     def __str__(self):
#         return self.itemCategory


class MenuItem(models.Model):
    itemid = models.AutoField(primary_key=True)
    itemName = models.CharField( max_length=50)
    itemPrice = models.FloatField(max_length=10)
    itemDescription = models.CharField( max_length=300)
    itemCategory = models.CharField(max_length=80,default='pizza')

    def __str__(self):
        return self.itemName


# class User(models.Model):   
#     userid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)
#     emailAddress = models.EmailField(max_length=100)
#     phone= models.CharField(max_length=11)
#     address= models.CharField(max_length=50)
#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     orderid = models.AutoField(primary_key=True)
#     userid = models.ForeignKey(User, on_delete=models.CASCADE)
#     total = models.FloatField(max_length=50)



# class OrderDetails(models.Model):
#     items = models.ManyToManyField(MenuItem)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     quantity = models.CharField(max_length=50)


   
class NewOrderTable(models.Model):
    name = models.CharField(max_length=60)
    emailAddress = models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    address= models.CharField(max_length=500, default = 'none')
    itemName  = models.CharField(max_length=500 )
    itemPrice = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    total = models.IntegerField()











