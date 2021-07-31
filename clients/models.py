from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(blank=False, null=False, max_length=120)
    short_code = models.CharField(blank=False, null=False, max_length=3)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name