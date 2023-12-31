# Generated by Django 4.2 on 2023-06-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Film İsmi')),
                ('image', models.ImageField(upload_to='movies/', verbose_name='Film Resmi')),
            ],
        ),
    ]
