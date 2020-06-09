from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.apps import apps
# Create your models here.

painting = apps.get_registered_model('Artists', 'Artistpainting')
categorypainting = apps.get_registered_model('Artists', 'Paintingofcategory')
# painting = apps.get_model('Artists', 'Artistpainting')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artistproduct = models.ForeignKey(painting, on_delete=models.CASCADE, default=None, null=True)
    categoryproduct = models.ForeignKey(categorypainting, on_delete=models.CASCADE, default=None, null=True)
    cartdate = models.DateTimeField(default=datetime.now())


STATUS_CHOICE = [
    ('pending', 'PENDING'),
    ('confirm', 'CONFIRM')
]


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artistproduct = models.ForeignKey(painting, on_delete=models.CASCADE, default=None, null=True)
    categoryproduct = models.ForeignKey(categorypainting, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=('pending', 'PENDING'))
    buydate = models.DateTimeField(default=datetime.now())
    orderid = models.IntegerField(default=1)


# confirm orders
# after payments