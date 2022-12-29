from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, FormView

from django.conf import settings

from .models import User
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
        if settings.ACCOUNT_LOGIN_UPON_REGISTRATION is True:
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


class AccountLogOut(LoginRequiredMixin, LogoutView):
    template_name = 'account/account_logout.html'


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
