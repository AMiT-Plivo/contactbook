from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Checks for valid email address before saving
        validator = EmailValidator()
        try:
            validator(self.email)
            super(Contact, self).save(*args, **kwargs)
        except ValidationError as e:
            raise e


