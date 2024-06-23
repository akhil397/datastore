from django.contrib import admin
from .models import CodeModels, Language, Types
# user-codestore pass - code1234


# Register your models here.
admin.site.register(CodeModels)
admin.site.register(Language)
admin.site.register(Types)


