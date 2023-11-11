from django import forms


class AnswerForm(forms.Form):
    text = forms.CharField(
        label='Ваш ответ:',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
    )