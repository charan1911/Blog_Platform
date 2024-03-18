from django.db import models
from datetime import datetime

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=100)

    image=models.ImageField(upload_to="images/")

    video=models.FileField(upload_to="media/")

    description=models.TextField()

    author=models.CharField(max_length=100)
    
    id = models.AutoField(primary_key=True)

    created_at=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title