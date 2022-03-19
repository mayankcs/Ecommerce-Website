from django.contrib import admin
from .models import category,product,productFeedback
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','price']
admin.site.register(product,productAdmin)
admin.site.register(category)
admin.site.register(productFeedback)