from django.db import models


class Filler(models.Model):
    FILLER_CHOICES = [
        ('chocolate', 'Шоколадные'),
        ('sugar_sprinkles', 'Сахарные присыпки'),
        ('fruits', 'Фрукты'),
        ('syrups', 'Сиропы'),
        ('jams', 'Джемы'),
    ]

    name = models.CharField(
        max_length=50,
        choices=FILLER_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    is_hit = models.BooleanField(default=False)
    fat = models.IntegerField(blank=False, null=False, default=0)
    fillers = models.ManyToManyField(Filler, related_name='products', blank=True, null=True)
