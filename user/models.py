from django.db import models


# Create your models here.
class User(models.Model):
    gender_type = {
        (0, 'girl'),
        (1, 'boy'),
    }
    gender = models.IntegerField(choices=gender_type, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
