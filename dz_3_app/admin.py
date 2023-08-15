from django.contrib import admin
from .models import User, Goods, Order


@admin.action(description='Сбросить количество до 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']
    ordering = ['price', '-quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    list_filter = ['title']
    actions = [reset_quantity]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['creation_date', 'user_ID', 'goods_ID', 'quantity', 'amount']
    ordering = ['creation_date']
    list_filter = ['creation_date', 'user_ID', 'goods_ID']

    # Отдельный заказ
    readonly_fields = ['creation_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['creation_date', 'user_ID', 'goods_ID'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'classes': ['collapse'],
                'fields': ['quantity', 'amount'],
            }
        ),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
