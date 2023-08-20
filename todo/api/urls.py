from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoListAPIView.as_view()),
    path('<int:todo_id>/', TodoDetailApiView.as_view())
]