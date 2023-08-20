from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TITLE_CHOICES = (
    ('1', 'Doing'),
    ('2', 'Not Start Yet'),
    ('3', 'Finish')
) 
class Todo(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField(blank= True, null= True)
    complete = models.CharField(max_length= 3, choices= TITLE_CHOICES, default= 1)
    timestamp = models.DateTimeField(auto_now_add= True, blank= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank= True, null= True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']