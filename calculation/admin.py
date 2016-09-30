from django.contrib import admin
from .models import ComplektSK, ComplektSKCalc


# class NameAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'weight')
#     search_fields = ('name',)

admin.site.register(ComplektSK)
admin.site.register(ComplektSKCalc)
