from django.db import models
# user-codestore pass - code1234


class CodeModels(models.Model):
    title = models.CharField(max_length=25)
    language = models.CharField(max_length=25)
    codes = models.TextField()
    description = models.TextField()
    types = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
