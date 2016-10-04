from django.contrib import admin
from .models import ComplektSK, ComplektSKCalc


# class NameAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'weight')
#     search_fields = ('name',)
class ComplektSKAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'price', 'weight')

admin.site.register(ComplektSK, ComplektSKAdmin)
admin.site.register(ComplektSKCalc)
