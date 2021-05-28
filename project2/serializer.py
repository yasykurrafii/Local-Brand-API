from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    type_pakaian = serializers.CharField(source = 'type_pakaian.type_pakaian', read_only=True)
    image = ImageURLSerializer(many = True, read_only=True)
    brand = BrandSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
    
# Django Rest Login
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']