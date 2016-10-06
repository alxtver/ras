from django.contrib import admin
from .models import ComplektSK, ComplektSKCal


# class NameAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'weight')
#     search_fields = ('name',)
class ComplektSKAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'price', 'weight')

admin.site.register(ComplektSK, ComplektSKAdmin)
