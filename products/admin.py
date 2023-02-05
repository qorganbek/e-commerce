from django.contrib import admin
from products import models


class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage
    extra = 1


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'is_top', 'is_active')
    inlines = (ProductImageInLine,)
    list_filter = ('is_top', 'is_active')
    list_editable = ('is_top', 'is_active')
    search_fields = ('title', 'body')


admin.site.register(models.Product, AdminProduct)
admin.site.register(models.ProductImage)
