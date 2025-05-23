# Generated by Django 5.2.1 on 2025-05-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_posts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='profile/posts/images'),
        ),
        migrations.AlterField(
            model_name='user_post',
            name='links',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
