from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    note = models.TextField()

    def __str__(self):
        return self.name