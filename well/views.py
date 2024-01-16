from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from well.forms import WellForm, LessonForm
from well.models import Well, Lesson


def index(request):
    return render(request, 'well/home.html')


@login_required
def contacts(request):
    return render(request, 'well/contacts.html')


class WellListView(LoginRequiredMixin, ListView):
    model = Well
    template_name = "well/well_list.html"


class WellCreateView(LoginRequiredMixin, CreateView):
    model = Well
    form_class = WellForm
    success_url = reverse_lazy("well:well-list")


class WellUpdateView(LoginRequiredMixin, UpdateView):
    model = Well
    form_class = WellForm
    success_url = reverse_lazy("well:well-list")


class WellDeleteView(LoginRequiredMixin, DeleteView):
    model = Well
    success_url = reverse_lazy("well:well-list")
    template_name = "well/well_confirm_delete.html"


class WellDetailView(LoginRequiredMixin, DeleteView):
    model = Well
    template_name = "well/well_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        well = get_object_or_404(Well, pk=self.kwargs['pk'])
        lessons = well.lessons.all()
        context['lessons'] = lessons
        return context


class LessonListView(LoginRequiredMixin, ListView):
    model = Lesson
    template_name = "well/lesson_list.html"


class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy("well:lesson-list")


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy("well:lesson-list")


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = Lesson
    success_url = reverse_lazy("well:lesson-list")
    template_name = "well/well_confirm_delete.html"


class LessonDetailView(LoginRequiredMixin, DeleteView):
    model = Lesson
    template_name = "well/lesson_detail.html"
