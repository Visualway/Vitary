from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('allauth/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.edit_profile, name='edit_profile'),
    path('profile/advance/', views.advanced_settings, name='advance_settings'),
    path('profile/advance/delete/', views.delete_account, name='delete_account'),
    path('profile/advance/change_username/',
         views.change_username, name='change_username'),

    path('following/', views.following, name='following'),
    path('followers/', views.followers, name='followers'),

]
