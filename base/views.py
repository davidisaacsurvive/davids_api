from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Todo
from base.serializers import TodoSerializer







# Create your views here.
def home(request):
    return JsonResponse({'message': 'Hello, world!'})

def todo_page(request):
    return render(request, 'base/todo_page.html')

class TodoListCreateView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):
    def get(self, request,pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(data={'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(instance=todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response(data={'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.delete()
            return Response(data={'message': 'Todo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response(data={'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response(data={'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
