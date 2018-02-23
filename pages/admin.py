from django.contrib import admin
from pages.models import *


class PizzaAdminInline(admin.TabularInline):
    model = Pizza
    extra = 2


class OrderModelAdmin(admin.ModelAdmin):
    inlines = [PizzaAdminInline]


admin.site.register(User)
admin.site.register(Address)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(Pizza)
admin.site.register(Topping)
