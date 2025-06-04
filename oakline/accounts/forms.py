from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        # Custom password rules
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password1):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', password1):
            raise ValidationError("Password must contain at least one number.")
        if not re.search(r'[\W_]', password1):
            raise ValidationError("Password must contain at least one special character.")

        return password2


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
