from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('termsandcondition/',views.termsandcondition,name='termsandcondition'),
    path('disclaimer/',views.disclaimer,name='disclaimer'),
    path('about/',views.about,name='about'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
]
] 