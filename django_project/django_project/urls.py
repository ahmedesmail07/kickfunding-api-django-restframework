from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('api.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent')

]

"""
END POINTS :
accounts/signup/[name='account_signup']
accounts/login/[name='account_login']
accounts/logout/[name='account_logout']
accounts/password/change/[name='account_change_password']
accounts/password/set/[name='account_set_password']
accounts/inactive/[name='account_inactive']
accounts/email/[name='account_email']
accounts/confirm-email/[name='account_email_verification_sent']
accounts/^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
accounts/password/reset/[name='account_reset_password']
accounts/password/reset/done/[name='account_reset_password_done']
accounts/^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
accounts/password/reset/key/done/[name='account_reset_password_from_key_done']
accounts/social/
"""
