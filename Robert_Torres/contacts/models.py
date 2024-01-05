from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    notes = models.TextField(blank=True, null=True)  # Add the notes field

    # Add other fields as needed

    def __str__(self):
        return self.name
