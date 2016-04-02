from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'signup_check',views.signupcheck),
    url(r'editprofile',views.editprofile),
    url(r'userprofile',views.userprofile),
    url(r'signup',views.signup),
]