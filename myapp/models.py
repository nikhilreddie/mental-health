from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100, default='')
    mobile = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    horror = models.BooleanField()
    action = models.BooleanField()
    science_fiction = models.BooleanField()
    thriller = models.BooleanField()
    comedy = models.BooleanField()
    romance = models.BooleanField()
    favourite_sports_and_places = models.TextField()
    intrests = models.TextField()
    goal = models.CharField(max_length=100, default= '')

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)  
    doctorName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    hospitalName = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=15)  
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.doctorName  

class Emotions(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    emotionname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}'s {self.emotionname} at {self.datetime}"
    
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    movieType = models.CharField(max_length=100)
    movieName = models.CharField(max_length=100)