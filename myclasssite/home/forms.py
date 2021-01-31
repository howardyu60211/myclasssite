from django import forms

# Create your forms here.

class UserForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
