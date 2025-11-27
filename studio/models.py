from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=150, blank=True)
    short_description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='trainers/', blank=True, null=True)

    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Порядок відображення")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
