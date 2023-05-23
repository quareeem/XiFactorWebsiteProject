from django.db import models

class PersonToContact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=16, default="DNE")
    email = models.EmailField()
    topic = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
