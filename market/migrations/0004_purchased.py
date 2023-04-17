# Generated by Django 4.1.7 on 2023-03-16 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_order_status_alter_car_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.car')),
            ],
        ),
    ]
