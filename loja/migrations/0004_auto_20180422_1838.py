# Generated by Django 2.0.4 on 2018-04-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20180422_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagemProduto',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
