# Generated by Django 4.2.6 on 2023-10-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blogs/%Y/%m/%d/'),
        ),
    ]
