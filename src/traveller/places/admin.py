from django.contrib import admin
from places.models import Place, Category, Gallery,Comments

class GalleryAdmin(admin.TabularInline):
    list_display = ["place","image"]
    model = Gallery



class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name","place","category"]
    
    inlines = [GalleryAdmin]
    
admin.site.register(Place,PlaceAdmin)
admin.site.register(Comments)
admin.site.register(Category)


