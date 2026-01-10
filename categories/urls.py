from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, CategoryListUserView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name="category_list_create"),
    path('<int:pk>/', CategoryDetailView.as_view(), name="category_detail"),
    path('categories/', CategoryListUserView.as_view(), name='user-categories'),
]
