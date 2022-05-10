from django.contrib import admin
from .models import Destinations, ClientReview , TourGallery

# Register your models here.

class users(admin.ModelAdmin):
    list_display= ('firstname', 'lastname','username', 'email')


    
admin.site.register(Destinations)
admin.site.register(ClientReview)
admin.site.register(TourGallery)


