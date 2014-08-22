from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.name