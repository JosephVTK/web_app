from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

# Create your views here.
class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile/user_profile.module.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.request.user, 'profile'):
            context['object'] = self.request.user.profile
        return context