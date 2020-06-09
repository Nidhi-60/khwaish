from django.contrib import admin
from .models import ArtistBlog, Feedback, Review

# Register your models here.
admin.site.register(ArtistBlog)
admin.site.register(Feedback)
admin.site.register(Review)
