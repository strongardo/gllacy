from django import forms


class NewsletterForm(forms.Form):
    email = forms.EmailField()


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=50)
