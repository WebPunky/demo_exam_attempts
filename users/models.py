from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r"^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    message="формат +7(XXX)-XXX-XX-XX"
)

class User(AbstractUser):
    phone = models.CharField("Телефон", max_length=20, validators=[phone_validator])
