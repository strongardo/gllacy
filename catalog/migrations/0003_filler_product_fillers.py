# Generated by Django 5.1.3 on 2024-12-19 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_fat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('chocolate', 'Шоколадные'), ('sugar_sprinkles', 'Сахарные присыпки'), ('fruits', 'Фрукты'), ('syrups', 'Сиропы'), ('jams', 'Джемы')], max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='fillers',
            field=models.ManyToManyField(blank=True, related_name='products', to='catalog.filler'),
        ),
    ]
