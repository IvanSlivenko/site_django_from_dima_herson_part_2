from django.contrib import admin
from market.models import Provider, Consumer, Category, Product, Order, OrderProduct, Store, SubCategory, InStock 

class ProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Provider, ProviderAdmin)

class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer, ConsumerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # pass
    list_display = ['name', 'get_small_image']
admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    # pass
    list_display = ['name', 'category', 'get_small_image']
admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    # pass
    list_display = ['name', 'in_stock', 'category','subcategory', 'get_small_image']
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)

class In_stockAdmin(admin.ModelAdmin):
    pass
admin.site.register(InStock, OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderProduct, OrderProductAdmin)

class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)
