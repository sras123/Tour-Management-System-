from distutils.command.upload import upload
from statistics import mode
from django.db import models



class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    # offer = models.BooleanField(default=False)

    
class ClientReview(models.Model):
    desc = models.TextField()
    user = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    

class TourGallery(models.Model):
    img= models.ImageField(upload_to='pics')
    gallerytitle = models.CharField(max_length=100)
    

    
    