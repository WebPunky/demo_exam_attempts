from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)


class Orders(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "новый"
        IN_PROGRESS = "in_progress", "в работе"
        DONE = "done", "выполнен"
        CANCELLED = "cancelled", "отменен"
    
    services = models.ForeignKey(
        Services,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders"
    )
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduledd_at = models.DateTimeField()


class Reviews(models.Model):
    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name="review"
    )
    rating = models.PositiveSmallIntegerField("Оценка", validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)