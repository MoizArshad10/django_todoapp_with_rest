from venv import create
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo.serializers import TodoSerializer
from todo.models import Todo

class ListTodoAPIVIEW(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIVIEW(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIVIEW(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIVIEW(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer