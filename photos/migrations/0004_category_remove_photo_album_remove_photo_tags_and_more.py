# Generated by Django 5.1.2 on 2024-11-06 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_album_tag_photo_album_photo_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='descriptionimage',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='upload_date',
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
