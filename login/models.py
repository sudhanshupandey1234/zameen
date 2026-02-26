from django.db import models

class loginm(models.Model):
    username=models.CharField(max_length=200)
    phone=models.IntegerField( )
    password=models.CharField( max_length=50)

    def __str__(self):
        return self.username



# Create your models here.
