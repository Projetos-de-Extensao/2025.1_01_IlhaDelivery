# Generated by Django 5.2 on 2025-06-04 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_statuspedido_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='quantidade',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
