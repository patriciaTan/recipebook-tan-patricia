from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 

from .models import Recipe, RecipeIngredient, Profile
# Register your models here.

class RecipeIngredient(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredient]


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInLine,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
