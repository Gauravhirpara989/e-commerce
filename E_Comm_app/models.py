from django.db import models
from django.utils.safestring import mark_safe

# username - ecomm
# password - 6767


class User(models.Model):

    user_status = (("Active", "Active"), ("Inactive", "Inactive"))

    Email_id = models.EmailField()
    Password = models.CharField(max_length=150)
    Name = models.CharField(max_length=150)
    Role = models.CharField(max_length=50, null=True)
    User_Status = models.CharField(max_length=150, choices=user_status, null=True)
    User_Address = models.TextField()
    User_Gender = models.CharField(max_length=20)
    User_DateofBirth = models.DateField(auto_now=True)
    User_Image = models.ImageField(upload_to="photos")

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.User_Image.url))


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


class Main_Category(models.Model):
    Main_Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Main_Category_Name


class Category(models.Model):
    Main_Category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    Category_Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Main_Category.Main_Category_Name + " -- " + self.Category_Name


class Sub_Category(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Sub_Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Category.Category_Name + " -- " + self.Sub_Category_Name


# class Sub_Category(models.Model):
#     Category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     Sub_Category_Name = models.CharField(max_length=150, null=True)

#     def __str__(self):
#         return self.Category.Category_Name+" -- "+self.Sub_Category_Name

# class Product_model(models.Model):
#     Sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
#     Product_Model_Name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.Sub_category.Sub_Category_Name+" -- "+self.Product_Model_Name


class Product(models.Model):

    Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=300)
    Product_Description = models.TextField(null=True)
    Product_Image_1 = models.ImageField(upload_to="photos",null=True)
    Product_Image_2 = models.ImageField(upload_to="photos",null=True)
    Product_Image_3 = models.ImageField(upload_to="photos",null=True)
    Product_Quantity = models.IntegerField()
    Product_Price = models.IntegerField()
    Product_Status = models.CharField(max_length=20)

    def Product_Photo_1(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Product_Image_1.url))
    
    def Product_Photo_2(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Product_Image_2.url))
    
    def Product_Photo_3(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Product_Image_3.url))


class Cart(models.Model):

    cart_status = (("0", "Confirm"), ("1", "Pending"))

    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cart_Quantity = models.IntegerField()
    Total_Amount = models.FloatField(null=True)
    Cart_Status = models.CharField(max_length=20, choices=cart_status,null=True)


class Order(models.Model):

    order_status = (("0", "Deliverd"), ("1", "Pending"))

    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Cart_Id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Payment_Method = models.CharField(max_length=20)
    Total_Amount = models.FloatField()
    Oreder_Status = models.CharField(max_length=10, choices=order_status)


class Card(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Card_Name = models.CharField(max_length=30)
    CVV = models.IntegerField()
    Expiry_Date = models.DateField()
    Card_Number = models.BigIntegerField()


class Payment(models.Model):

    payment_status = (("0", "Success"), ("1", "Failed"))

    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Order_Id = models.ForeignKey(Order, on_delete=models.CASCADE)
    Total_Amount = models.IntegerField()
    Payment_Status = models.CharField(max_length=15, choices=payment_status)


class FeedBack(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Comment = models.TextField()
    Rating = models.IntegerField()


class Complain(models.Model):

    complain_status = (("0", "Solved"), ("1", "Pending"))

    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment = models.TextField()
    Complain_Date = models.DateField()
    Complain_Status = models.CharField(max_length=20, choices=complain_status)


class Wishlist(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Create_Date = models.DateField()
