from django import forms


class FilterForm(forms.Form):
    FILLER_CHOICES = [
        ('chocolate', 'Шоколадные'),
        ('sugar_sprinkles', 'Сахарные присыпки'),
        ('fruits', 'Фрукты'),
        ('syrups', 'Сиропы'),
        ('jams', 'Джемы'),
    ]

    fat = forms.CharField(max_length=25, required=False)
    fillers = forms.MultipleChoiceField(
        choices=FILLER_CHOICES,
        required=False,
    )
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)

