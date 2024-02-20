from django.contrib import admin
from .models import *

# Register your models here.


class user_info(admin.ModelAdmin):
    list_display = [
        "Email_id",
        "Password",
        "Name",
        "Role",
        "User_Status",
        "User_Address",
        "User_Gender",
        "User_DateofBirth",
        "User_Image",
    ]


admin.site.register(User, user_info)


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

# class Sub_Category_info(admin.ModelAdmin):
#     list_display = ["Category", "Sub_Category_Name"]


# admin.site.register(Sub_Category, Sub_Category_info)


# class Product_model_info(admin.ModelAdmin):
#     list_display = ["Sub_category","Product_Model_Name"]


# admin.site.register(Product_model, Product_model_info)


class Product_info(admin.ModelAdmin):
    list_display = [
        "Sub_Category",
        "Product_Name",
        "Product_Description",
        "Product_Image",
        "Product_Quantity",
        "Product_Price",
        "Product_Status",
    ]


admin.site.register(Product, Product_info)


class Cart_info(admin.ModelAdmin):
    list_display = ["User_Id", "Product_Id", "Cart_Quantity","Total_Amount","Cart_Status"]


admin.site.register(Cart, Cart_info)


class Order_info(admin.ModelAdmin):
    list_display = [
        "User_Id",
        "Cart_Id",
        "Payment_Method",
        "Total_Amount",
        "Oreder_Status",
    ]


admin.site.register(Order, Order_info)


class Card_info(admin.ModelAdmin):
    list_display = ["User_Id", "Card_Name", "CVV", "Expiry_Date", "Card_Number"]


admin.site.register(Card, Card_info)


class Payment_info(admin.ModelAdmin):
    list_display = ["User_Id", "Order_Id", "Total_Amount", "Payment_Status"]


admin.site.register(Payment, Payment_info)


class FeedBack_info(admin.ModelAdmin):
    list_display = ["User_Id", "Product_Id", "Comment", "Rating"]


admin.site.register(FeedBack, FeedBack_info)


class Complain_info(admin.ModelAdmin):
    list_display = ["User_Id", "Comment", "Complain_Status", "Complain_Date"]


admin.site.register(Complain, Complain_info)


class Wishlist(admin.ModelAdmin):
    list_display = ["User_id", "Product_Id", "Create_Date"]
