from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from well.models import Well


def index(request):
    return render(request, 'well/home.html')


def contacts(request):
    return render(request, 'well/contacts.html')


class WellListView(LoginRequiredMixin, ListView):
    model = Well


