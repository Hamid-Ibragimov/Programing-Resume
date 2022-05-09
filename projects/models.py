from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    name              = models.CharField(max_length=120)
    language          = models.CharField(max_length=120)
    description       = models.TextField(blank=True, null=True)
    image             = models.ImageField()
    popup_media       = models.FileField(blank=True, null=True)
    popup_source_link = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse('projects:project', kwargs={'id': self.id})