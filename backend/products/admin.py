from django.contrib import admin
from .models import Product, ProductVariant


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "category",
        "is_active",
        "created_at",
    )

    list_filter = ("is_active", "category", "brand")
    search_fields = ("name", "brand", "category")
    inlines = [ProductVariantInline]

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "product",
        "size",
        "color",
        "cost_price",
        "wholesale_price",
    )

    list_filter = ("size", "color")
    search_fields = ("sku", "product__name")

    
