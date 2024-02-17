from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length = 100)
    image_url = models.CharField(max_length = 100, blank = True)
    body = models.CharField(max_length = 1000000)
    created_at = models.DateTimeField("date published",default = datetime.now, blank = True)

    def __str__(self):
        return f"{self.title}"