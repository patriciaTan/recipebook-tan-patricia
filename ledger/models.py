from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    shortBio = models.TextField(
        validators=[
            MinLengthValidator(255, 'This field must contain at least 255 characters.')
        ]
    )

    def __str__(self):
        return "{}".format(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self): 
        return reverse('ledger:recipe_list',args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile, 
        null=True,
        default=None,
        on_delete=models.CASCADE,
        related_name='users'
    )
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updateOn = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail',args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
       Ingredient,
       on_delete=models.CASCADE,
       related_name='recipe' 
    )
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )


