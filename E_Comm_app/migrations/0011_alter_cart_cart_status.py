# Generated by Django 5.0.3 on 2024-03-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Comm_app', '0010_cart_order_id_alter_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_Status',
            field=models.CharField(choices=[('Confirm', 'Confirm'), ('Pending', 'Pending')], max_length=20, null=True),
        ),
    ]
