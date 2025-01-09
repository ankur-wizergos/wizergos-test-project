# myapp/models.py

from django.db import models
from .tasks import my_task
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    result = my_task.delay(3, 5)
    def __str__(self):
        return self.title


