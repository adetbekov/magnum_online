from django.contrib import admin
from .models import Product, Point, Transaction, Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0


class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ('name','category','created')
    list_filter=['category']
    search_fields=['name','category']


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name','created')
    search_fields=['name']
    inlines = [SubCategoryInline]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name','subcategory','created','price','available')
    list_filter=['available']
    search_fields=['name','price']


class PointAdmin(admin.ModelAdmin):
    model = Point
    list_display = ('name','real_address','open_time','close_time')
    search_fields=['name','real_address']


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('user','created','status','qr_hash')
    list_filter=['status']
    search_fields=['user','qr_hash']
    filter_horizontal = ('cart',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Transaction, TransactionAdmin)