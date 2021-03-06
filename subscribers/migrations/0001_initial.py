# Generated by Django 2.0.1 on 2018-01-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('application', models.CharField(choices=[('blog', 'blog'), ('fragments', 'fragments')], max_length=16, verbose_name='Application')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail address')),
                ('subscribed', models.DateTimeField(auto_now_add=True, verbose_name='Date of subscription')),
                ('confirmed', models.DateTimeField(blank=True, null=True, verbose_name='Date of confirmation')),
                ('last_notified', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Date of last notification')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Date of last update')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ('email',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together={('email', 'application')},
        ),
    ]
