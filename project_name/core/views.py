from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect

from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib import messages
from django.core.mail import send_mail


class HomeView(TemplateView):
    template_name = 'pages/home.html'

home = cache_page(60 * 10)(HomeView.as_view())
