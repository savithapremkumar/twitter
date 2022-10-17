from django.db import models


class Tweet(models.Model):
    message = models.CharField(max_length=50)
    name = models.CharField(max_length=140)
    datetime = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        ordering = ['name', 'datetime']
