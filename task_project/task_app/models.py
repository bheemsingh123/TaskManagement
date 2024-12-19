from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title