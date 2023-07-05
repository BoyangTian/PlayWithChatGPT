from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# 'format' input can control request and response type
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
@api_view(['GET', 'POST'])
def task_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def task_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def task_detail(request, pk):
#     """
#     Retrieve, update or delete a code task.
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(task, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         task.delete()
#         return HttpResponse(status=204)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)