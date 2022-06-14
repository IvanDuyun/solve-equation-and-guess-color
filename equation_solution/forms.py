from django import forms

class Equation(forms.Form):
    a = forms.FloatField(label='a')
    b = forms.FloatField(label='b')
    c = forms.FloatField(label='c')