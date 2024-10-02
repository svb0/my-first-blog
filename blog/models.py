from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db import connections



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Student(models.Model):
    host = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    class Meta:
        db_table = "think_info"