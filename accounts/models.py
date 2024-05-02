from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass  # 추가 필드가 필요하다면 여기에 정의할 수 있음.
