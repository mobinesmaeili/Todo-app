from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    created_at = forms.DateTimeField()
