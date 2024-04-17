from django.contrib import admin
from .models import Phone, Repair, Accessory, Photo

# Register your models here.
admin.site.register(Phone)
admin.site.register(Repair)
admin.site.register(Accessory)
admin.site.register(Photo)