# Generated by Django 5.0.1 on 2024-02-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Comm_app', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
