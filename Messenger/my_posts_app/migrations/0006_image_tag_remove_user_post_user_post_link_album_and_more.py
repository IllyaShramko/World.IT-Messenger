# Generated by Django 5.2 on 2025-06-15 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_posts_app', '0005_images_post_author_alter_user_post_links'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=150)),
                ('file', models.ImageField(upload_to='images/posts/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_post',
            name='user',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=4096)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.profile')),
                ('images', models.ManyToManyField(blank=True, related_name='posts_authored', to='my_posts_app.image')),
                ('likes', models.ManyToManyField(blank=True, related_name='posts_liked', to='user_app.profile')),
                ('views', models.ManyToManyField(blank=True, related_name='posts_viewed', to='user_app.profile')),
                ('tags', models.ManyToManyField(blank=True, to='my_posts_app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_posts_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='images/album_previews')),
                ('shown', models.BooleanField(default=True)),
                ('images', models.ManyToManyField(blank=True, to='my_posts_app.image')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_posts_app.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Images_Post',
        ),
        migrations.DeleteModel(
            name='User_Post',
        ),
    ]
