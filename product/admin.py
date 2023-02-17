from django.contrib import admin
from .models import Color, Size, Product, Information
# Register your models here.
class informationsAdmin(admin.StackedInline):
    model = Information

@admin.register(Product)
class productaAmin(admin.ModelAdmin):
    inlines = (informationsAdmin,)
    list_display = ('title', 'price')





admin.site.register(Color)
admin.site.register(Size)