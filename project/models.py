from django.db import models
class Signup(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    

    def _str_(self):
        return self.name

# Create your models here.
