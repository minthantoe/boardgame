"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views as main_views
from chess import views as chess_views
from checkers import views as checkers_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', chess_views.UserViewSet)
router.register(r'chess', chess_views.ChessViewSet)
router.register(r'checkers', checkers_views.CheckersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name = 'home'),
    path('chess', chess_views.home, name = 'chess'),
    path('chessLocal', chess_views.local, name = 'chess_local'),
    path('chessAI', chess_views.ai, name = 'chess_ai'),
    path('chessHistory', chess_views.history, name = 'chess_history'),
    path('chessLeaderboard', chess_views.home, name = 'chess_leaderboard'),
    path('checkers', checkers_views.home, name = 'checkers'),
    path('checkersHistory', checkers_views.history, name = 'checkers_history'),
    path('about', main_views.about, name = 'about'),
    path('join/', main_views.join, name='join'),
    path('login/', main_views.login, name='login'),
    path('logout/', main_views.logout, name='logout'),
    path('api/v1/', include(router.urls)),
    path('api-auth/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
