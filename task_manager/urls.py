from django.urls import path
from .views import register, TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, LoginAPIView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
]
