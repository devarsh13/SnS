from django.conf.urls import include, url
import views

urlpatterns = [
    
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
    
    url(r'productdetail',views.product_details),
    url(r'login',views.login),
    url(r'sendrequest',views.send_request),
    url(r'reportproduct',views.report_product),
    url(r'confirmdeal',views.confirm_post),
    url(r'productresults',views.category_products),
    url(r'getchats',views.chat_history_data),
    url(r'addchat',views.add_chat),
    url(r'verify',views.verify_user),
    url(r'forgotpassword',views.forgot_password),
    url(r'getusers',views.send_users),
    url(r'admin',views.admin_data),
    url(r'deleteuser',views.delete_user),
    url(r'deleteproduct',views.delete_product),
    url(r'notifications',views.notifications)
]
	
