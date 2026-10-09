from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class TaskList(APIView):
    def get(self, request):
        tas = Task.objects.all()
        serializer = TaskSerializer(tas, many=True)
        return Response(serializer.data)


class TaskCreate(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, )

class ContactDetail(APIView):
    def get(self, request, pk):
        tas = get_object_or_404(Task, id=pk)
        serializer = TaskSerializer(tas)
        return Response(serializer.data)

class ContactDelete(APIView):
    def delete(self, request, pk):
        tas = get_object_or_404(Task, id=pk)
        tas.delete()
        return Response({'deleted': True})

class ContactUpdate(APIView):
    def put(self, request, pk):
        tas = get_object_or_404(Task, id=pk)
        serializer = TaskSerializer(tas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ContactPatch(APIView):
    def patch(self, request, pk):
        tas = get_object_or_404(Task, id=pk)
        serializer = TaskSerializer(tas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
