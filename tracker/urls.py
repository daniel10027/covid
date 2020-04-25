from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PaysListView, Search, LocaliteListView


urlpatterns = [
  path('', PaysListView.as_view(), name='site-home'),
  path('search/', Search.as_view(), name='search'),
  path('country/<str:nom>/', LocaliteListView.as_view(), name='pays-detail'),
]
