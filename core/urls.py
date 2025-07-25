from django.urls import path
from . import views
# from .views import SignUpView, UserLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('clubs/', views.clubs_dropdown, name='clubs_dropdown'),
    path('leagues/', views.leagues, name='leagues'),
    path('statistic/', views.statistics, name='team_statistic'),
    # path('register/', SignUpView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<slug:slug>/', views.club_detail, name='club_detail'),
]
