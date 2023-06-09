# Generated by Django 4.2.1 on 2023-05-20 15:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Carrito',
                'db_table': 'Carrito',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodoPago', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Metodo de pago',
                'db_table': 'Metodo de pago',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Stock',
                'db_table': 'Stock',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('tipo_usuario', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre', models.CharField(max_length=40)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.categoria')),
                ('id_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.stock')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Prod_carrito',
            fields=[
                ('id_prod_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.carrito')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.producto')),
            ],
            options={
                'verbose_name': 'Productos en Carrito',
                'db_table': 'Productos en Carrito',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('suma_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('estado', models.CharField(max_length=30)),
                ('id_metodoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.metodopago')),
                ('id_prod_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.prod_carrito')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.usuario')),
            ],
            options={
                'verbose_name': 'Orden',
                'db_table': 'Orden',
            },
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id_detalleOrden', models.AutoField(primary_key=True, serialize=False)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.orden')),
            ],
            options={
                'verbose_name': 'Detalle de la orden',
                'db_table': 'Detalle de la orden',
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededatos.usuario'),
        ),
    ]
