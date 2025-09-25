from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Category(models.TextChoices):
    WORK = "WK", "Work"
    PERSONAL = "PSNL", "Personal"
    IDEAS = "IDEAS", "Ideas"


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(choices=Category.choices, max_length=5, default=Category.PERSONAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
