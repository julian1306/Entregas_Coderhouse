# Generated by Django 4.0.4 on 2022-07-04 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_productos_new_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muebles_exterior',
            fields=[
                ('productos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='productos.productos')),
                ('resistencia', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('productos.productos',),
        ),
    ]
