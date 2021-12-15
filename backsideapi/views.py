from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from .models import MenuItem,NewOrderTable
from .serializers import MenuItemSerializer,OrderBySeriliazer
from django.utils.html import escape
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

@api_view(['GET'])
def getMenu (request):
    Menu = MenuItem.objects.all()
    serializer = MenuItemSerializer(Menu,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postOrderDetails (request):
    # order = NewOrderTable.objects.all()
    # # Menu = MenuItem.objects.all()
    # serializer = OrderBySeriliazer(order,many = True)
    # print(request.body)
    # return Response(serializer.data)
    order = JSONParser().parse(request)
    serializer = OrderBySeriliazer(data=order)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getOrderDetails (request):
    order = NewOrderTable.objects.all()
    # Menu = MenuItem.objects.all()
    serializer = OrderBySeriliazer(order,many = True)
    return Response(serializer.data)