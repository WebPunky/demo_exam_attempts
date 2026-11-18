from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Поля: логин (уникальный), пароль (не менее 6 символов),
# повтор пароля, ФИО (только кириллица, пробелы, дефис), телефон
# ( +7(XXX)-XXX-XX-XX ), email. Все поля обязательны.

class User(AbstractUser):
    phone = models.CharField("Телефон", max_length=20)