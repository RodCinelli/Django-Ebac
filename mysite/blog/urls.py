from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('post/', views.PostView.as_view(), name='post')  # Nova URL
]
