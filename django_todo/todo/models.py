from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=122)
    body = models.CharField(max_length=122)
    is_completed = models.BooleanField(default=False)
    date = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_created=True)

    def __str__(self):
        return self.title