# Generated by Django 5.2 on 2025-06-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_produto_alter_itempedido_quantidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuspedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Pago', 'Pago'), ('Em Preparo', 'Em Preparo'), ('Em Transporte', 'A caminho'), ('Entregue', 'Entregue'), ('Cancelado', 'Cancelado')], max_length=50),
        ),
    ]
