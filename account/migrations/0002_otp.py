# Generated by Django 4.1.6 on 2023-02-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('randomcode', models.IntegerField()),
                ('expertion_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]