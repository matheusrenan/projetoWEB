# Generated by Django 2.0.4 on 2018-04-21 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(max_length=120)),
                ('descricaoCategoria', models.TextField(default='texto default')),
            ],
        ),
        migrations.CreateModel(
            name='loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField(default='texto default')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomeProduto', models.CharField(max_length=120)),
                ('descricaoProduto', models.TextField(default='texto default')),
                ('imagemProduto', models.FileField(blank=True, upload_to='static/%Y/%m/%d')),
                ('precoProduto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.Categoria')),
            ],
        ),
    ]
