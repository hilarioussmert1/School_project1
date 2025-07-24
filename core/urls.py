from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('clubs/', views.clubs_dropdown, name='clubs_dropdown'),
    path('leagues/', views.leagues, name='leagues'),
    path('statistic/', views.statistics, name='team_statistic'),
    path('<slug:slug>/', views.club_detail, name='club_detail'),
]