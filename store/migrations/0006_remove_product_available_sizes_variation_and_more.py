# Generated by Django 5.0.3 on 2024-03-28 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cartitem_size'),
        ('store', '0005_remove_product_available_quantities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_sizes',
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('talla', 'talla')], max_length=100)),
                ('variation_value', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]