# Generated by Django 3.1.5 on 2021-04-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('web', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('publishdate', models.DateField(auto_now=True)),
            ],
        ),
    ]
