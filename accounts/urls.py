from django.urls import path

from .views import CreateUserView, LoginUserView

urlpatterns = [
    path('', CreateUserView.as_view()),
    path('login', LoginUserView.as_view()),
]
