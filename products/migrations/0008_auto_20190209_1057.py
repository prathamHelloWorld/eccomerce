# Generated by Django 2.0.6 on 2019-02-09 10:57

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190209_1043'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('custom_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
