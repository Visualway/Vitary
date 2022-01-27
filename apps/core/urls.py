from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_to_home),
    path('home/', views.home, name='home'),
    path('u/', views.peoples, name='peoples'),
    path('explore/', views.explore, name='explore'),
    path('report/<int:pk>/', views.report_abuse, name='report_abuse'),
    path('404/', views.page_404),
    path('search/', views.search, name='search'),
    path('terms/', views.terms, name='terms'),
    path('badge/<int:pk>/', views.badge, name='badge'),
    path('donate/', views.donate, name='donate'),
    path('all-donations/', views.all_donations, name='all_donations'),
    path('my-donations/', views.my_donations, name='my_donations'),
    path('request-badge/<int:pk>/', views.request_badge, name='request_badge'),
]
