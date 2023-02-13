# Generated by Django 4.1.6 on 2023-02-11 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=300, unique=True)),
                ('Slug', models.SlugField(max_length=300, unique=True)),
                ('categoryImage', models.ImageField(blank=True, upload_to='category_img')),
                ('categoryDescription', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('categoryName',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=300, unique=True)),
                ('Slug', models.SlugField(max_length=300, unique=True)),
                ('productImage', models.ImageField(blank=True, upload_to='category_img')),
                ('productDescription', models.TextField(blank=True)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('productAvailable', models.BooleanField(default=True)),
                ('productStock', models.IntegerField()),
                ('productCreatedAt', models.DateField(auto_now_add=True)),
                ('productUpdatedAt', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rej_home.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('productName',),
            },
        ),
    ]
