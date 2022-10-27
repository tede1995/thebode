from django.contrib import admin
from .models import Post, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)

admin.site.site_header  =  "TheBode Admin"  
admin.site.site_title  =  "TheBode Admin"
admin.site.index_title  =  "TheBode Admin"