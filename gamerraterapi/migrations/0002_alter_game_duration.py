# Generated by Django 4.0.6 on 2022-07-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
