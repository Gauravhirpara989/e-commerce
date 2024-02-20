# Generated by Django 5.0.2 on 2024-02-09 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Comm_app', '0006_slider_product_image_dark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_Category_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=150)),
                ('Main_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.main_category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Category_Name', models.CharField(max_length=150, null=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Model_Name', models.CharField(max_length=200)),
                ('Sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Comm_app.sub_category')),
            ],
        ),
    ]