from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'signupcheck',views.signup_check),
    url(r'editprofiledata',views.editprofile),
    url(r'editprofile',views.edit_profile_change),
    url(r'userprofile',views.userprofile),
    url(r'signup',views.signup),
    url(r'dashboard',views.dashboard),
    url(r'settings',views.settings),
    url(r'changepassword',views.change_password),
    url(r'transactions',views.transactions),
    url(r'updaterating',views.change_rating),
    url(r'myposts',views.my_posts),
    url(r'deletepost',views.delete_my_posts),
    url(r'updatepost',views.update_my_posts),
    url(r'deleteaccount',views.delete_account),
    url(r'reportuser',views.report_a_user),
    url(r'createpost',views.create_post),
    url(r'editpost',views.edit_post),
    url(r'editdata',views.edit_data),
    url(r'sendmail',views.send_email),
    url(r'productdetail',views.product_details),
    url(r'login',views.login),
    url(r'sendrequest',views.send_request),
    url(r'reportproduct',views.report_product),
    url(r'confirmdeal',views.confirm_deal)
]
	