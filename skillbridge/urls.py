from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/beneficiaries/', include('beneficiaries.urls')),
    path('api/v1/trainers/', include('trainers.urls')),
    
]
