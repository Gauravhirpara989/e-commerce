# Generated by Django 5.0.1 on 2024-01-16 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_name', models.CharField(max_length=150)),
                ('Card_no', models.BigIntegerField()),
                ('CVV', models.IntegerField()),
                ('Expiry_date', models.CharField(max_length=150)),
                ('Amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_quantity', models.IntegerField()),
                ('Cart_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirm', 'Confirm')], max_length=150)),
                ('Total_Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=150)),
                ('User_email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=150)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_id', models.EmailField(max_length=254)),
                ('Phone_no', models.BigIntegerField()),
                ('Password', models.IntegerField()),
                ('Name', models.CharField(max_length=150)),
                ('Store_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_id', models.EmailField(max_length=254)),
                ('Password', models.IntegerField()),
                ('Name', models.CharField(max_length=150)),
                ('Gender', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('User_image', models.ImageField(upload_to='photos')),
                ('Phone_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_status', models.CharField(choices=[('Place Order', 'Place Order'), ('Pending', 'Pending')], max_length=150)),
                ('Product_quantity', models.IntegerField()),
                ('Total_amount', models.IntegerField()),
                ('Cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.cart')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.ImageField(upload_to='photos')),
                ('Product_name', models.CharField(max_length=150)),
                ('Product_description', models.TextField()),
                ('Product_status', models.CharField(choices=[('Avilable', 'Available'), ('Unavilable', 'Unavilable')], max_length=150)),
                ('Product_price', models.IntegerField()),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.category')),
                ('Store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.store')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='Product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.product'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_type', models.CharField(max_length=150)),
                ('Payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirm', 'Confirm')], max_length=150)),
                ('payment_Datetime', models.DateTimeField(auto_now=True)),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.order')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.CharField(max_length=150)),
                ('Rating', models.IntegerField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Time_Stamp', models.DateTimeField(auto_now=True)),
                ('complain_status', models.CharField(choices=[('Pending', 'Pending'), ('Solved', 'Solved')], max_length=150)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.user'),
        ),
    ]
