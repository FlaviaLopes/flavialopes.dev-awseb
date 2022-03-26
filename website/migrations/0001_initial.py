# Generated by Django 4.0.2 on 2022-03-06 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('introduction', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar1', models.ImageField(default='avatar1.png', upload_to='')),
                ('avatar2', models.ImageField(default='avatar2.png', upload_to='')),
                ('name_card', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HeadTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_url', models.CharField(default='https://flavialopes.dev', max_length=200)),
                ('og_type', models.CharField(default='website', max_length=200)),
                ('og_title', models.CharField(max_length=200)),
                ('og_description', models.CharField(max_length=200)),
                ('og_image', models.ImageField(default='logo.png', upload_to='')),
                ('og_site_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=20)),
                ('keywords', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ShareOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network_name', models.CharField(max_length=30)),
                ('social_network_link', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network_name', models.CharField(max_length=30)),
                ('social_network_link', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
