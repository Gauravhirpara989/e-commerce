# Generated by Django 5.0.2 on 2024-02-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Comm_app', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Product_Id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Cart_Id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Main_Category',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='Product_Id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Order_Id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Sub_Category',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='Product_Id',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='User_id',
        ),
        migrations.DeleteModel(
            name='User_details',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Main_Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Complain',
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Sub_Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
