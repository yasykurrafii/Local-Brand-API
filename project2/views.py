from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, Group

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializer import BrandSerializer,ProductSerializer, TypeSerializer

from .models import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'List': {
            'GET' : 'http://127.0.0.1:8000/api/brand',
            'DELETE': '/task-create/'
        },
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def BrandList(request):
    if request.method == 'GET':
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
    elif request.method == 'POST':
        serializer = BrandSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Sukses dimasukan!')
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProductType(request, tp):
    tipe = Type.objects.get(type_pakaian=tp)
    baju = Product.objects.filter(type_pakaian=tipe.id)
    serializer = ProductSerializer(baju, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProductList(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def DetailProduct(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance = product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated!")
        return Response('Data not Update')
    elif request.method =='DELETE':
        product.delete()
        return Response('Item successfully deleted!')

@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated])
def DetailBrand(request,pk):
    brand = Brand.objects.get(id = pk)
    if request.method == 'GET':
        serializer = BrandSerializer(brand, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BrandSerializer(instance = brand, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated!")
        return Response('Data not Update')
    elif request.method =='DELETE':
        brand.delete()
        return Response('Item successfully deleted!')



# @api_view(['GET'])
# def TaskDetail(request, pk):
#     tasks = Task.objects.get(id = pk)
#     serializer = TaskSerializer(tasks, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def TaskCreate(request):
#     serializer = TaskSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST', 'GET'])
# def TaskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     if request.method == 'POST':
#         serializer = TaskSerializer(instance=task, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response("Data has been updated!")
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)

# @api_view(['DELETE','GET'])
# def TaskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response('Item successfully deleted!')
    
    



    