# Generated by Django 2.2.6 on 2020-01-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200107_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='tier',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='total_games',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='winrate',
            field=models.FloatField(null=True),
        ),
    ]
