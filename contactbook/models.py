from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=20)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name


