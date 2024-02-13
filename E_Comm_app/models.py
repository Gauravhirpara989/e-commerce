from django.db import models
from django.utils.safestring import mark_safe

# username - ecomm
# password - 6767


class Slider(models.Model):
    Discount_deals = (
        (
            "Get 20% off on all laptops and smartphones.",
            "Get 20% off on all laptops and smartphones.",
        ),
        (
            "Bundle offer: Buy a TV and soundbar together and save 15%.",
            "Bundle offer: Buy a TV and soundbar together and save 15%.",
        ),
        (
            "Stay Connected: Save 15% on all smartwatches.",
            "Stay Connected: Save 15% on all smartwatches.",
        ),
        ("Save $20 on your purchase!", "Save $20 on your purchase!"),
    )

    Product_Image = models.ImageField(upload_to="photos")
    Product_Image_dark = models.ImageField(upload_to="photos", null=True)
    Discount_deals = models.CharField(max_length=150, choices=Discount_deals)
    Sale = models.IntegerField()
    Brand_Name = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Product_link = models.CharField(max_length=100)

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Product_Image.url))

    def product_photo_dark(self):
        return mark_safe(
            '<img src="{}" width="100"/>'.format(self.Product_Image_dark.url)
        )

    def __str__(self):
        return self.Brand_Name


class user(models.Model):
    Email_id = models.EmailField()
    Password = models.CharField(max_length=150)
    Name = models.CharField(max_length=150)
    Role = models.CharField(max_length=50, null=True)
    # Status


# class details(models.Model)
#     address,gender,dob,dp


class Main_Category(models.Model):
    Main_Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Main_Category_Name


class Category(models.Model):
    Main_Category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    Category_Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Category_Name + " -- " + self.Main_Category.Main_Category_Name


class Sub_Category(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Sub_Category_Name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.Sub_Category_Name+" -- "+self.Category.Category_Name


class Product_model(models.Model):
    Sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    Product_Model_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Product_Model_Name
