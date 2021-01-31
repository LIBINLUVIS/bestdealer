from django.contrib import admin
from .models import image,comment,userprofile,userphone

# Register your models here.
admin.site.register(image)
admin.site.register(comment)
admin.site.register(userprofile)
admin.site.register(userphone)
