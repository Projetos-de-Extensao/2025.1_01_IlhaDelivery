# Generated by Django 5.2 on 2025-06-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_pedido_forma_pagamento_alter_pedido_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
