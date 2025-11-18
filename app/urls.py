from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),

    # logowanie / wylogowanie / rejestracja
    path('login/', auth_views.LoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='game_list'), name='logout'),
    path('register/', views.register, name='register'),
]
