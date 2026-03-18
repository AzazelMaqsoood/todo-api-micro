from django.db import models

class Task(models.Model):
    PRIOTIY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIOTIY_CHOICES, default="medium")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    