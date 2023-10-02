from django.contrib import admin

from toys.models import Brend, Toy, Category, Item, Order

# Register your models here.
admin.site.register(Toy)
admin.site.register(Brend)
admin.site.register(Category)


class ItemInline(admin.TabularInline):
    model = Item
    fields = ['product', 'quantity', 'price']
    raw_id_fields = ['product']
    readonly_fields = ['price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'creator', 'status', 'total_price']
    list_filter = ['created_at']
    inlines = [ItemInline]



