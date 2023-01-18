from django.contrib import admin
from . import models 

@admin.register(models.Pizza)
class PizzaModelAdmin(admin.ModelAdmin):
    list_display = ['topping1', 'topping2', 'size']


@admin.register(models.Size)
class PizzaModelAdmin(admin.ModelAdmin):
    list_display = ['title']