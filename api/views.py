from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer, TodoSerializerForUpdate
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TodoListAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        todos = Todo.objects.all()
        todos_serializer = TodoSerializer(todos, many=True)
        return Response(todos_serializer.data)


class TodoAddAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id
        todo_serializer = TodoSerializer(data=data)
        if todo_serializer.is_valid(raise_exception=True):
            todo_serializer.save()
            return Response(todo_serializer.data)
        return Response({'message': 'Error'})


class UpdateDestroyAPiView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ()

    def get_object(self, pk):
        return Todo.objects.get(pk=pk)

    def put(self, request, pk):
        try:
            todo = self.get_object(pk)
            data = TodoSerializerForUpdate(todo, request.data)
            data.is_valid(raise_exception=True)
            data.save()

        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)

        return Response({'Success': True})

    def patch(self, request, pk):
        try:
            todo = self.get_object(pk)
            data = TodoSerializerForUpdate(todo, request.data, partial=True)
            data.is_valid(raise_exception=True)
            data.save()

        except Exception as e:
            return Response({'Success': False, 'message': e}, status=400)

        return Response({'Success': True})

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response({'Success': True})
