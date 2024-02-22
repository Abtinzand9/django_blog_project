from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super(PublishedManager ,self).get_queryset().filter(status = 'published')


class Article(models.Model):
    """a class to make articles"""

    # make the status choices
    STATUS_OF_ARTICLES = (
        ('checking' , 'Checking'),
        ('rejected' , 'Rejected'),
        ('published' , "Published")
    )

    title = models.CharField(max_length =50)
    body = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name = 'Articles')
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 15 ,choices = STATUS_OF_ARTICLES , default = 'checking')

    class Meta:
        ordering = ("create_date",)

    def __str__(self):
        """method returns title"""
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    objects = models.Manager()
    publish = PublishedManager()