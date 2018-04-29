from django.contrib import admin
from .models import Product, Transaction


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name','created','price','available')
    list_filter=['available']
    search_fields=['name','price']


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('user','created','status','qr_hash')
    list_filter=['status']
    search_fields=['user','qr_hash']
    filter_horizontal = ('cart',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)