from django.contrib import admin

from .models import Services, Orders, Reviews

# Register your models here.
@admin.register(Services)
class CustomServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "price",]
    list_filter = ["price",]

@admin.register(Orders)
class CustomOrdersAdmin(admin.ModelAdmin):
    list_display = ["status"]

@admin.register(Reviews)
class CustomReviewAdmin(admin.ModelAdmin):
    list_display = ["rating", ]
    list_filter = ["rating",]
    