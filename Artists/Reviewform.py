from django import forms
from django.apps import apps

review = apps.get_model('Blogs', 'Review')


# user = models.ForeignKey(User, on_delete=models.CASCADE)
#     review = models.CharField(max_length=200)
#     artist = models.ForeignKey(artistpainting, null=True, default=None, on_delete=models.CASCADE)
#     category = models.ForeignKey(categorypainting, null=True, default=None, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=datetime.now())


class Review(forms.ModelForm):
    class Meta:
        model = review
        review = forms.CharField(widget=forms.Textarea())
        fields = [
            "review",
        ]
        exclude = [
            "user",
            "artist",
            "category",
            "created_date"
        ]

