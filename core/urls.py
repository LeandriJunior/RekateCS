from django.urls import re_path
import core.views
urlpatterns = [
    re_path('home', core.views.HomeView.as_view(), name='home')
]