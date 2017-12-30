from django.db import models
from django.utils import timezone


# Create your models here.
class File(models.Model):

    file_no = models.IntegerField()
    file_name = models.CharField(max_length=200)
    file_content = models.CharField(max_length=400)
    file_path = models.CharField(max_length=200)
    upload_date = models.DateTimeField(null=True, blank=True)

    def upload(self):
        self.upload_date = timezone.now()
        self.save()

    def __str__(self):
        return self.file_name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
