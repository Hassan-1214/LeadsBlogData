# Generated by Django 4.2.5 on 2023-11-24 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LDHapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_description', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('main_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('blog_author', models.CharField(blank=True, max_length=100, null=True)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('catg_views', models.IntegerField(default=0)),
                ('blog_image', models.ImageField(blank=True, help_text='Image size: Width=1301 pixel. Height=556 pixel', null=True, upload_to='media/')),
                ('blog_isactive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catg_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(default='authorimage.jpg', null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='catg_author',
        ),
        migrations.DeleteModel(
            name='AuthorModel',
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.AddField(
            model_name='blog',
            name='catg_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LDHapp.categorie'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag_name',
            field=models.ManyToManyField(to='LDHapp.tag'),
        ),
    ]