# Generated by Django 5.1.2 on 2024-11-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]