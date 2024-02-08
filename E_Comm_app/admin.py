from django.contrib import admin
from .models import user, Slider

# Register your models here.


class user_info(admin.ModelAdmin):
    list_display = ["Email_id", "Password", "Name", "Role"]


admin.site.register(user, user_info)


class Slider_info(admin.ModelAdmin):
    list_display = [
        "product_photo",
        "product_photo_dark",
        "Discount_deals",
        "Sale",
        "Brand_Name",
        "Discount",
        "Product_link",
    ]


admin.site.register(Slider, Slider_info)
