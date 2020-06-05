from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='styles/images')
    model = models.FileField(upload_to='styles/models')

    def __str__(self):
        return str(self.name)