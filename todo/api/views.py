from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from todo.models import Todo
from .serializers import TodoSerializer

class TodoListAPIView(APIView):
    #add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description':request.data.get('description'),
            'complete': request.data.get('complete'),
            'user': request.user.id
        }
        serializer = TodoSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        try:
            return Todo.objects.get(id= todo_id, user= user_id)
        except Todo.DoesNotExist:
            return None
        
    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status= status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'description':request.data.get('description'),
            'complete': request.data.get('complete'),
            'user': request.user.id
        }
        serializer = TodoSerializer(instance= todo_instance, data= data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status= status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {'res':'Object deleted!'},
            status= status.HTTP_200_OK
        )