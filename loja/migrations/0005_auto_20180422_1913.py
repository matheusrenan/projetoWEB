# Generated by Django 2.0.4 on 2018-04-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_auto_20180422_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
