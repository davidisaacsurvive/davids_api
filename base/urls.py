from django.urls import path
from base.views import home, TodoListCreateView, TodoDetailView, TodoListFilteredView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



urlpatterns = [
    path('',home, name='home'),
    path('todos/',TodoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<str:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/filtered/', TodoListFilteredView.as_view(), name='todo-filtered'),
    path('api/schema/', SpectacularAPIView.as_view(), name='model-schema'),
    path('api/v1/docs/',SpectacularRedocView.as_view(url_name='model-schema'), name='redoc'),
    path('api/v2/docs/',SpectacularSwaggerView.as_view(url_name='model-schema'),name='swagger-ui'),

]