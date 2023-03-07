from django.urls import path, include
from django.conf import settings

from .views import AccountCreateView, AccountPasswordResetCompleteView, AccountChangeView
from .views import AccountProfileView, AccountLogIn, AccountLogOut, AccountPasswordResetView, AccountPasswordResetConfirmView, AccountPasswordResetDoneView
from .views import AccountPasswordChangeView, AccountPasswordChangeDoneView, AccountInactiveView, AccountTwoFactorAuthenticateView

urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='account_create'),
    path('login/', AccountLogIn.as_view(), name='account_login'),
    path('logout/', AccountLogOut.as_view(), name='account_logout'),
    path('status/inactive/', AccountInactiveView.as_view(), name='account_inactive'),
    path('status/authenticate/', AccountTwoFactorAuthenticateView.as_view(), name='account_two_factor_authenticate'),
    path('edit/', AccountChangeView.as_view(), name='account_edit'),
    path('password/', AccountPasswordChangeView.as_view(), name='account_password_change'),
    path('password/changed/', AccountPasswordChangeDoneView.as_view(), name='account_password_change_complete'),

    path('password/reset/', AccountPasswordResetView.as_view(), name='account_password_reset'),
    path('password/reset/done/', AccountPasswordResetDoneView.as_view(), name='account_password_done'),
    path('password/reset/complete/', AccountPasswordResetCompleteView.as_view(), name='account_password_complete'),
    path('password/__reset__/<str:uidb64>/<str:token>/', AccountPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

if 'user_profile.apps.UserProfileConfig' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('profile/', include('user_profile.urls'))
    ]

else:
    urlpatterns += [
        path('profile/', AccountProfileView.as_view(), name='profile_detail')
    ]

