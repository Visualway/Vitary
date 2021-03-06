from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_home),
    path('home/', views.home, name='home'),
    path('user/', views.peoples, name='peoples'),
    path('explore/', views.explore, name='explore'),
    path('report/<int:pk>/', views.report_abuse, name='report_abuse'),
    path('404/', views.page_404),
    path('search/', views.search, name='search'),
    path('badge/<int:pk>/', views.badge, name='badge'),
    path('dashboard/', views.redirect_to_profile, name='dashboard'),
]
