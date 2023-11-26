from django.urls import path
from .views import TodoAddAPIView, UpdateDestroyAPiView, TodoListAPIView
urlpatterns = [
    path('todo-list', TodoListAPIView.as_view(), name='todo_list'),
    path('create-todo', TodoAddAPIView.as_view(), name='create_todo'),
    path('todo/<int:pk>', UpdateDestroyAPiView.as_view(), name='update_todo'),
]
