from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializers

# Create your views here.


class TaskViews(generics.CreateAPIView):
    model            = Task
    serializer_class = TaskSerializers

class GetTaskViews(generics.ListAPIView):
    queryset        = Task.objects.all()
    serializer_class= TaskSerializers

class UpdateTaskViews(generics.UpdateAPIView):
    queryset        = Task.objects.all()
    serializer_class= TaskSerializers

class DeleteTaskViews(generics.DestroyAPIView):
    queryset        = Task.objects.all()
    serializer_class= TaskSerializers