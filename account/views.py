import uuid

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, FormView

from django.conf import settings
from django.utils import timezone

from django.forms import ValidationError

from .models import User, TwoFactorToken
from .forms import RegistrationForm, UserEditForm

# Create your views here.


class AccountCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/account_create.html'
    success_url = reverse_lazy('account_profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Automatically Login the User
        if settings.ACCOUNT_2FA is True:
            return HttpResponseRedirect(reverse('account_two_factor_authenticate'))
        elif settings.ACCOUNT_LOGIN_UPON_REGISTRATION is True:
            user = authenticate(
                self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user:
                login(self.request, user=user)

        return response


class AccountChangeView(FormView):
    model = User
    form_class = UserEditForm
    template_name = 'account/account_create.html'
    success_url = reverse_lazy('account_profile')


class AccountProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account_profile.html'


class AccountLogIn(LoginView):
    template_name = 'account/account_login.html'

    def form_valid(self, form):
        user = form.get_user()

        if settings.ACCOUNT_2FA and not user.is_two_factor_authenticated:
            user.send_two_factor_authentication()
            return HttpResponseRedirect(reverse('account_inactive'))

        return super().form_valid(form)


class AccountLogOut(LoginRequiredMixin, LogoutView):
    template_name = 'account/account_logout.html'


class AccountTwoFactorAuthenticateView(TemplateView):
    template_name = 'account/account_two_factor_authenticate.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        username = request.GET.get('username')

        if not token or not username:
            print('No token or username')
            return HttpResponseRedirect(reverse('index_page'))

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print('User does not exist')
            return HttpResponseRedirect(reverse('index_page'))

        if user.is_two_factor_authenticated is True:
            print('User already authenticated.')
            return HttpResponseRedirect(reverse('index_page'))

        if not hasattr(user, 'twofactortoken'):
            self.extra_context['reissue'] = True
            user.send_two_factor_authentication()
            print('User does not have token.')
            return super().get(request, *args, **kwargs)

        try:
            auth_token = TwoFactorToken.objects.get(
                user=user, token=uuid.UUID(token))
        except TwoFactorToken.DoesNotExist:
            print('Token does not exist.')
            return HttpResponseRedirect(reverse('index_page'))

        if auth_token.is_valid() is False:
            self.extra_context['expired'] = True
            self.extra_context['token'] = auth_token
            self.extra_context['now'] = timezone.now()
            user.send_two_factor_authentication()
            print(f'Token is expired')
            return super().get(request, *args, **kwargs)

        print('All good.')
        # We have passed
        auth_token.delete()
        user.is_two_factor_authenticated = True
        user.save()
        self.extra_context['authenticated'] = True

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class AccountInactiveView(TemplateView):
    template_name = 'account/account_inactive.html'


class AccountPasswordResetView(PasswordResetView):
    """_summary_

    Args:
        PasswordResetView (_type_): _description_

    Functionality:
        AccountPasswordResetView -> AccountPasswordResetDoneView -> __Send Email__
        __Email Link__ -> AccountPasswordResetConfirmView -> AccountPasswordResetCompleteView

    """
    template_name = 'account/account_password_reset.html'
    success_url = reverse_lazy('account_password_done')


class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/account_password_reset_done.html'


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/account_password_reset.html'
    success_url = reverse_lazy('account_password_complete')


class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/account_password_reset_complete.html'


class AccountPasswordChangeView(PasswordChangeView):
    template_name = 'account/account_password_change.html'
    success_url = reverse_lazy('account_password_change_complete')


class AccountPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/account_password_change_done.html'
