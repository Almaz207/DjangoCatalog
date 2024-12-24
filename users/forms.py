from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser


class CustomUserCreatingForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    user_name = forms.CharField(max_length=20, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_name', 'phone_number', 'password1', 'password2',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Телефон может состоять только из цифр')
        return phone_number
