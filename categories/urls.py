from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    # List all categories & create a new one
    path('', CategoryListCreateView.as_view(), name="category_list_create"),

    # Retrieve, update, delete by ID
    path('<int:pk>/', CategoryDetailView.as_view(), name="category_detail"),
]
