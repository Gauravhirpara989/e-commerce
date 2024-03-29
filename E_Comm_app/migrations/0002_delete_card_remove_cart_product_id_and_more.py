# Generated by Django 5.0.2 on 2024-02-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Comm_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='User_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Cart_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Category_id',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='User_id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='User_id',
        ),
        migrations.DeleteModel(
            name='Inquiry',
        ),
        migrations.RemoveField(
            model_name='order',
            name='User_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='User_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Store_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Complain',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
