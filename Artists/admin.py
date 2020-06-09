from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Artist)
admin.site.register(models.Artistpainting)
admin.site.register(models.Paintingcategory)
admin.site.register(models.Paintingofcategory)
