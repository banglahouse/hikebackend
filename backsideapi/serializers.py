from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import  MenuItem,NewOrderTable

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        
        fields = ('__all__')


# class CategorySerializer(serializers.ModelSerializer):
#     menu = MenuItemSerializer()

#     class Meta:

#         model = Category
#         fields = ('__all__')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '___all__'


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         depth = 1
#         fields = ('orderid','userid','total')


# class OrderDetailSeriliazer(serializers.ModelSerializer):
#     orders = OrderSerializer(many = True)
#     user= UserSerializer(many = True)
#     class Meta:
#         model = OrderDetails
#         depth = 1
#         fields = ('items', 'order', 'quantity' ,'orders','user')


class OrderBySeriliazer(serializers.ModelSerializer):
    class Meta:
        model = NewOrderTable
        depth = 1
        fields= '__all__'