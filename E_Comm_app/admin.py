from django.contrib import admin
from .models import *

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


class Main_Category_info(admin.ModelAdmin):
    list_display = ["Main_Category_Name"]


admin.site.register(Main_Category, Main_Category_info)


class Category_info(admin.ModelAdmin):
    list_display = ["Main_Category", "Category_Name"]


admin.site.register(Category, Category_info)


class Sub_Category_info(admin.ModelAdmin):
    list_display = ["Category", "Sub_Category_Name"]


admin.site.register(Sub_Category, Sub_Category_info)


class Product_model_info(admin.ModelAdmin):
    list_display = ["Sub_category","Product_Model_Name"]


admin.site.register(Product_model, Product_model_info)
