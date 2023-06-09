# Generated by Django 4.1.3 on 2023-03-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='movie',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='music',
            field=models.FileField(default=22, upload_to='audiofiles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
