# Generated by Django 3.1.5 on 2021-05-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0017_auto_20210509_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.PositiveIntegerField(),
        ),
    ]
