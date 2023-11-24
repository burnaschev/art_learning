from django.urls import path

from well.apps import WellConfig
from well.views import index, contacts, WellListView

app_name = WellConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('well/list', WellListView.as_view(), name='well-list')

]
