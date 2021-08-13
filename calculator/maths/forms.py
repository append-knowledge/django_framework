from django import forms


class CalculationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()


class Cube(forms.Form):
    num=forms.IntegerField()