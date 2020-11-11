from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from new.models import Todo
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from new.serializers import TodoSerializer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
# Create your views here.
@csrf_exempt
@api_view(['GET','POST','DELETE','PUT'])
def todolist(request, pk=None):
    if request.method=='GET':
        qs=Todo.objects.all()
        serializer=TodoSerializer(instance=qs,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            msg=serializer.validated_data['message']
            Todo.objects.create(
                message=msg
            )
            return Response({"status":"ok"})

        return Response(serializer.errors)

    elif request.method=='DELETE':
        listid=Todo.objects.get(pk=pk)
        listid.delete()
        return Response({"msg":"Deleted"})

    elif request.method=="PUT":
        listid=Todo.objects.get(pk=pk)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            msg = serializer.validated_data['message']
            listid.message=msg
            listid.save()
            return Response({"status": "ok"})

        return Response(serializer.errors)