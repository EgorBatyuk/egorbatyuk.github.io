from django import forms


class ReviewForm(forms.Form):
    author_name = forms.CharField(label='Ваше имя', max_length=100)
    review = forms.CharField(label='Отзыв', max_length=100)