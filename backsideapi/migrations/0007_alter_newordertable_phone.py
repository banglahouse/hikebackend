# Generated by Django 3.2.9 on 2021-12-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backsideapi', '0006_auto_20211215_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newordertable',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
