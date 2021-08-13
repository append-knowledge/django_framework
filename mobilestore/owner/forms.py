from django import forms

class SignUp(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    user_name=forms.CharField()
    password=forms.CharField()
    conform_password=forms.CharField()


class SignIn(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField()


class AddMobile(forms.Form):
    company=forms.CharField()
    model_name=forms.CharField()
    colour=forms.CharField()
    price=forms.IntegerField()
    available_pieces=forms.IntegerField()