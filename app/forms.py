from django import forms

class Transactions(forms.Form):
    apple = forms.CharField(max_length=100)
    banana = forms.CharField(max_length=100)
    grapes = forms.CharField(max_length=100)
    papaya = forms.CharField(max_length=100)
    cherries = forms.CharField(max_length=100)