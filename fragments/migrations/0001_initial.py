# Generated by Django 2.0.1 on 2018-01-25 16:31

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('content', markdownx.models.MarkdownxField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Date published')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ('-published',),
                'get_latest_by': 'published',
            },
        ),
    ]
