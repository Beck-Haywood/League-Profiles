# Generated by Django 2.2.6 on 2020-01-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200107_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
