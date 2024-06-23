from django.db import models

class Language(models.Model):
    lang_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.lang_name

class Types(models.Model):
    Type_of_code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Type_of_code

class CodeModels(models.Model):
    title = models.CharField(max_length=25)
    code_lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    codes = models.TextField()
    description = models.TextField()
    type_code = models.ForeignKey(Types, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
