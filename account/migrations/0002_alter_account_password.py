# Generated by Django 4.1.5 on 2023-04-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=25),
        ),
    ]
