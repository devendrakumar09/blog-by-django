from django.db import models

# Create your models here
from ckeditor.fields import RichTextField

class Category(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')  
  title = models.CharField(max_length=255)
  description = RichTextField()
  slug = models.SlugField()
  post_date = models.DateField(null=True)
  visible_in_menu = models.BooleanField(default=False)
  
  def __str__(self):
    return f"{self.title}"


class Blog(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = RichTextField()
  thumbnail = models.ImageField()
  slug = models.SlugField()
  featured = models.BooleanField(default=False)
  post_date = models.DateField(null = True)  

  def __str__(self):
    return f"{self.title}"
