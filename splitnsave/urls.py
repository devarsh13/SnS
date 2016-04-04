from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'signupcheck',views.signup_check),
    url(r'editprofiledata',views.editprofile),
    url(r'editprofile',views.edit_profile_change),
    url(r'userprofile',views.userprofile),
    url(r'signup',views.signup),
]