# Generated by Django 4.2 on 2023-04-22 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0004_cart_quantity_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='unit_price',
        ),
        migrations.AlterField(
            model_name='cart',
            name='menuitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonAPI.menuitem'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='LittleLemonAPI.order'),
        ),
    ]
