# Generated by Django 4.1.6 on 2023-02-11 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rej_home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Slug',
            new_name='slug',
        ),
    ]
