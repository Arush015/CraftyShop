# Generated by Django 2.2.14 on 2020-11-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201112_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='post_pic/'),
        ),
    ]
