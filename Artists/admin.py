from django.contrib import admin
from . import models
from django.contrib.admin import AdminSite
# Register your models here.


AdminSite.site_header = "Khwaish Art Gallary"
AdminSite.index_title = "Khwaish"
AdminSite.site_title = "Admin"


admin.site.register(models.Artist)
admin.site.register(models.Artistpainting)
admin.site.register(models.Paintingcategory)
admin.site.register(models.Paintingofcategory)