# Generated by Django 5.1.2 on 2024-11-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_category_options_alter_photo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
