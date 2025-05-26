from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect

from .views import custom_logout_view

#def custom_logout_view(request):
#    messages.success(request, "✅ Вы успешно вышли из аккаунта.")
#   return auth_views.LogoutView.as_view(next_page='article_list')(request)

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
# Авторизация
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='article_list'), name='logout'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', views.register, name='register'),

# Поисковик
    path('search/', views.search_articles, name='search_articles'),

#  О Нас
   path('about/', views.about_page, name='about_page'),
]


