from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.author_list, name='author_list'),
    path('', views.home, name='home'),  # Add this line
]
