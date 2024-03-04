from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail'),
]

app_name = 'ledger'
