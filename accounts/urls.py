from django.urls import path

from .views import CreateUserView, LoginUserView, UserProfileAPIView

urlpatterns = [
    path('', CreateUserView.as_view()),
    path('login', LoginUserView.as_view()),
    path('<str:username>', UserProfileAPIView.as_view()),
]