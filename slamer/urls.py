from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fsignup',views.fetch_signup,name='fetch_signup'),
    path('register',views.signup,name='signup'),
    path('flogin',views.fetch_login,name='fetch_login'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.fetch_home,name='fetch_home'),
    path('usearch',views.usearch,name='usearch'),
    path('pprofile',views.pub_profile,name='pub_profile'),
    path('prprofile',views.priv_profile,name='priv_profile'),
    path('fupprofile',views.fetch_update_profile,name='fetch_update_profile'),
    path('upprofile',views.update_profile,name='update_profile'),
    path('fslam_form',views.fetch_slam_form,name='fetch_slam_form'),
    path('reqslam',views.request_slam,name='request_slam'),
    path('slampost',views.slam_poster,name='slam_poster'),
    path('slam',views.fetch_slam,name='fetch_slam'),
    path('pptoggle',views.pub_priv_toggle,name='pub_priv_toggle'),
    path('slamwipe',views.slam_delete,name='slam_delete'),
]
