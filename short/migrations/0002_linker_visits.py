# Generated by Django 3.1.3 on 2020-11-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linker',
            name='visits',
            field=models.IntegerField(default=0, verbose_name='Visits'),
        ),
    ]
