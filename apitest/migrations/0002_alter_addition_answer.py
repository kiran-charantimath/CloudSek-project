# Generated by Django 3.2.7 on 2021-09-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='answer',
            field=models.IntegerField(default=None, null=True),
        ),
    ]