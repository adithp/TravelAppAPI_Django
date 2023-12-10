from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="places/images/")
    place = models.CharField(max_length=200)
    category = models.ForeignKey("places.Category",on_delete=models.CASCADE)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = "places_place"
        
    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(upload_to="categories/images/")
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = "places_category"
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name
    
    
class Gallery(models.Model):
    place = models.ForeignKey("places.Place",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="places/images/")
    
    class Meta:
        db_table = "places_gallery"
        verbose_name_plural = "gallery"
        
    def __str__(self):
        return str(self.id)
    

class Comments(models.Model):
    description = models.TextField()
    published_date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey("places.Place",on_delete=models.CASCADE)
    class Meta:
        db_table = "places_comment"
        verbose_name_plural = "comments"
        
    def __str__(self):
        return str(self.id)
    

    
    