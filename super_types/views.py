from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def type_list(request):
    
    if request.method =='GET':

        serializer = SuperTypeSerializer(many=True)   
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)