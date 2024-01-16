from django.urls import path

from well.apps import WellConfig
from well.views import index, contacts, WellListView, WellDeleteView, WellUpdateView, WellCreateView, WellDetailView, \
    LessonListView, LessonCreateView, LessonUpdateView, LessonDeleteView, LessonDetailView

app_name = WellConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('well/list', WellListView.as_view(), name='well-list'),
    path('well/create', WellCreateView.as_view(), name='well-create'),
    path('well/update/<int:pk>', WellUpdateView.as_view(), name='well-update'),
    path('well/delete/<int:pk>', WellDeleteView.as_view(), name='well-delete'),
    path('well/<int:pk>', WellDetailView.as_view(), name='well-view'),

    path('lesson/list', LessonListView.as_view(), name='lesson-list'),
    path('lesson/create', LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/update/<int:pk>', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>', LessonDeleteView.as_view(), name='lesson-delete'),
    path('lesson/<int:pk>', LessonDetailView.as_view(), name='lesson-view'),
]
