from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from datetime import datetime
# get artist model
artistmodel = apps.get_registered_model('Artists', 'Artist')
artistpainting = apps.get_registered_model('Artists', 'Artistpainting')
categorypainting = apps.get_registered_model('Artists', 'Paintingofcategory')
# Create your models here.


# artist detail
class ArtistBlog(models.Model):
    artist = models.ForeignKey(artistmodel, on_delete=models.CASCADE)
    dob = models.DateTimeField()
    painting = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    awards = models.CharField(max_length=200)


# Customer feedback
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=300)


# Customer review about the product
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    artist = models.ForeignKey(artistpainting, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(categorypainting, null=True, default=None, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now())
