from django.contrib import admin

# Register your models here.

from .models import Blog,Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
