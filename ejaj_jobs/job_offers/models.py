from django.db import models

# Create your models here.
class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.title