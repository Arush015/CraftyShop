# Generated by Django 2.2.14 on 2020-11-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201112_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='post_pic/'),
        ),
    ]
