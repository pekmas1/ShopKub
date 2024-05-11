from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class Meta:
        ordering = ("user", )
 
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    tel_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True)