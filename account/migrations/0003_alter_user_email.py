# Generated by Django 4.1.6 on 2023-02-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
    ]
