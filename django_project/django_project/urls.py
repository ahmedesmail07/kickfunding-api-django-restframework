from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView,
SpectacularSwaggerView,
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(
        url_name="schema"), name="redoc",),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(
        url_name="schema"), name="docs"), 
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# TODO: @ahmedesmail07
# ? I Update the URL for account to be api/accounts/ so it matches both my APIs and yours
# ? for example yours: api/accounts/login/  ||  mine:  api/projects/

# ? Also update gitignore file to ignore all cache files and db.SQLite3

"""
END POINTS :
For All Auth Not JSON
api/accounts/signup/[name='account_signup']
api/accounts/login/[name='account_login']
api/accounts/logout/[name='account_logout']
api/accounts/password/change/[name='account_change_password']
api/accounts/password/set/[name='account_set_password']
api/accounts/inactive/[name='account_inactive']
api/accounts/email/[name='account_email']
api/accounts/confirm-email/[name='account_email_verification_sent']
api/accounts/^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
api/accounts/password/reset/[name='account_reset_password']
api/accounts/password/reset/done/[name='account_reset_password_done']
api/accounts/^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
api/accounts/password/reset/key/done/[name='account_reset_password_from_key_done']
api/accounts/social/
"""
