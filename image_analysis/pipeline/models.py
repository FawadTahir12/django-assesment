from django.db import models
from django.contrib.postgres.fields import ArrayField


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email


class ImageAnalysis(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="images_analysis")
    images = ArrayField(models.JSONField(),blank=True, default=None)  
    analysis_data =models.JSONField(default=None)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis Report for {self.user.email}"