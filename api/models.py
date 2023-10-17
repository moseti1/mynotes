from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.body[0:50]
    
