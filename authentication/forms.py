from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email',)


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError(_('Password does not match'))

        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        
        if user:
            raise forms.ValidationError(_('Username already exists'))
        
        return username

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user