from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',auth_views.signin,name='signin'),
    path('termsandcondition/',views.termsandcondition,name='termsandcondition'),
    path('disclaimer/',views.disclaimer,name='disclaimer'),
    path('about/',views.about,name='about'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('cart/',views.cart,name='cart'),
    path('buying/',views.buying,name='buying'),
]
