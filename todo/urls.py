from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TaskList.as_view(), name= 'list'),
    path('login/', Login.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name= 'logout'),
    path('register/', Register.as_view(), name= 'register'),
    path('task_detail/<int:pk>', TaskDetail.as_view(), name= 'detail'),
    path('create_task',TaskCreate.as_view(), name= 'create'),
    path('update_task/<int:pk>', TaskUpdate.as_view(), name= 'update'),
    path('delete_task/<int:pk>', DeleteTask.as_view(), name= 'delete'),
    path('api/', include('todo.api.urls')),
    path('todo/', TODOListView.as_view(), name= 'todo'),
    path('todo/<str:pk>/', TODODetailView.as_view(), name= 'todo-detail')
]
