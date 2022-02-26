from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import CustomUserModel


class CustomUserCreateForm(forms.ModelForm):

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = ('name',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Password don't match"))
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class CustomUserChangeFormInAdmin(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUserModel
        fields = (
            'name', 'phone', 'first_name', 'last_name', 'avatar',
            'date_birth', 'slug', 'is_active', 'is_admin',
        )
