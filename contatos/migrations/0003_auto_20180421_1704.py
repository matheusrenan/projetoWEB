# Generated by Django 2.0.4 on 2018-04-21 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20180421_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]