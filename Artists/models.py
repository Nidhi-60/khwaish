from django.db import models

# Create your models here.


# artist detail
class Artist(models.Model):
    artistname = models.CharField(max_length=50)
    artistimage = models.ImageField(default='errorimage/noimage.png', upload_to='Image/')
    specialist = models.CharField(max_length=50)


# painting of artist
class Artistpainting(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    paintingname = models.CharField(max_length=50)
    paintingimage = models.ImageField(default='errorimage/noimage.png', upload_to='Image/Artist/')
    paintingtype = models.CharField(max_length=20)
    paintingsize = models.CharField(max_length=50)
    paintingprice = models.IntegerField(default=0)
    paintingcode = models.CharField(max_length=2, default='A')


# painting type
class Paintingcategory(models.Model):
    paintingcategoryname = models.CharField(max_length=50)
    paintingimage = models.ImageField(default='errorimage/noimage.png', upload_to='Image/Category/')


# painting of category
class Paintingofcategory(models.Model):
    categoryid = models.ForeignKey(Paintingcategory, on_delete=models.CASCADE)
    paintingimage = models.ImageField(default='errorimage/noimage.png', upload_to='Image/Category/')
    paintingname = models.CharField(max_length=50)
    paintingsize = models.CharField(max_length=50)
    paintingprice = models.IntegerField(default=0)
    paintingcode = models.CharField(max_length=2, default='C')

