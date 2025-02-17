from django.contrib import admin
from .models import Product, Filler


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)  # запятая обязательна


admin.site.register(Product, ProductAdmin)
admin.site.register(Filler)
