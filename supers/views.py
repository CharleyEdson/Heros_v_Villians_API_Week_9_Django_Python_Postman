from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import super_types
from .serializers import SuperSerializer
from .models import Super
from rest_framework import status
from django.shortcuts import get_object_or_404

from supers import serializers
# Create your views here.

@api_view(['GET', 'POST'])
def hero_list(request):
    
    if request.method =='GET':

        type_of_super = request.query_params.get('super_type')
       
        queryset = Super.objects.all()
        if type_of_super:
            queryset = queryset.filter(super_type__type=type_of_super)
            
        serializer = SuperSerializer(queryset, many=True)   
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def hero_details(request,pk):
    hero = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(hero);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(hero, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)