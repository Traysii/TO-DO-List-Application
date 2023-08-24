from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TODOSerializer
from .permissions import IsOwner

# Create your views here.
class Login(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')
    

class Register(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(Register, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'tasks'
    template_name = 'todo/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count1'] = context['tasks'].filter(complete = '1').count()
        context['count2'] = context['tasks'].filter(complete = '2').count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todo/detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list')
    template_name = 'todo/form.html'

    def form_valid(self, form):
        form.instance.user  = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list')
    template_name = 'todo/form.html'

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('list')
    template_name = 'todo/confirm_delete.html'


class TODOListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TODOSerializer
    permission_classes = (IsAuthenticated, )

class TODODetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TODOSerializer
    permission_classes = (IsOwner, )




# def list(request):
#     tasks = Todo.objects.all()

#     form = TodoForm()
    
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             return redirect('todo')
#             # return HttpResponse("<h2>Save not successfully! </h2>")

#     context = {'tasks': tasks, 'form': form}
#     return render(request, 'base.html', context)

# def update(request, pk):
#     task = Todo.objects.get(id=pk)

#     form = TodoForm(instance= task)

#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance= task)
#         if form.is_valid():
#             form.save()
#             return redirect('todo')
#         else:
#             return redirect('todo')
#             # return HttpResponse("<h2>Save not successfully! </h2>")

#     context = {'form': form}
#     return render(request, 'update.html', context)

# def delete(request, pk):
#     item = Todo.objects.get(id=pk)

#     if request.method == 'POST':
#         item.delete()
#         return redirect('todo')

#     context = {'item': item}
#     return render(request, 'delete.html', context)
