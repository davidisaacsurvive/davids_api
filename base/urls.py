from django.urls import path
from base.views import home, TodoListCreateView, TodoDetailView


urlpatterns = [
    path('',home, name='home'),
    path('todos/',TodoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<str:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]