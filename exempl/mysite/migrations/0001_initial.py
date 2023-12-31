# Generated by Django 4.2.5 on 2023-09-19 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Desc')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('date', models.DateField(verbose_name='Date')),
                ('image', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=2000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Coment',
                'verbose_name_plural': 'Coments',
            },
        ),
    ]
