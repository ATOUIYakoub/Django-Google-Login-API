from django.urls import path
from . import views
from .views import GoogleLoginApi


urlpatterns = [
      path("auth/login/google/", GoogleLoginApi.as_view()),
]