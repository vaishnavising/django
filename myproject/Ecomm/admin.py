from unicodedata import category
from django.contrib import admin

from .models import order, register_info,product,Category


# Register your models here.
# class_register_dtls(admin.ModelAdmin):
# list_display=['firstname','lastname','email']
# admin.site.register(register_info, register_dtls)
admin.site.register(register_info)
admin.site.register(product)
admin.site.register(Category)
admin.site.register(order)


