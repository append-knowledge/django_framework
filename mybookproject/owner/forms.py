from django import forms

class AddBookForm(forms.Form):
    book_name=forms.CharField()
    author=forms.CharField()
    price=forms.IntegerField()
    copies=forms.IntegerField()

class EditBook(forms.Form):
    book_id=forms.IntegerField()
    book_name=forms.CharField()
    price = forms.IntegerField()
    copies = forms.IntegerField()

class RemoveBook(forms.Form):
    book_id = forms.IntegerField()
    book_name = forms.CharField()

class SignUp(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    user_name=forms.CharField()
    password=forms.CharField()
    conform_password=forms.CharField()


class SignIn(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField()

