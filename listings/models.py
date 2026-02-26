from django.db import models
from django.contrib.auth.models import User
class listings(models.Model):
    Room_title= models.CharField(max_length=100)
    Room_rent= models.IntegerField( )
    Room_images1=models.ImageField(upload_to='room_images/', blank=True, null=True)
    Room_images2=models.ImageField(upload_to='room_images/', blank=True, null=True)
    Room_images3=models.ImageField(upload_to='room_images/', blank=True, null=True)
    Room_images4=models.ImageField(upload_to='room_images/', blank=True, null=True)
    Room_images5=models.ImageField(upload_to='room_images/', blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True , null=True)
    Room_details= models.TextField()
    Room_available=models.BooleanField(default=True)
    Room_type=models.CharField(max_length=50)
    Room_security=models.IntegerField(default=000 )
    wifi=models.BooleanField(default=False)
    bed=models.BooleanField(default=False)
    mattres=models.BooleanField(default=False)
    table=models.BooleanField(default=False)
    chair=models.BooleanField(default=False)
    fan=models.BooleanField(default=False)
    Ac=models.BooleanField(default=False)
    ro=models.BooleanField(default=False)

    def __str__(self):
        return self.Room_title
    
class Booking(models.Model):
    
    listings = models.ForeignKey(listings, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.Room_title}"

# Create your models here.
class RoomBooking(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    check_in_date = models.DateField()

    payment_done = models.BooleanField(default=False)

    feedback = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.check_in_date}"
