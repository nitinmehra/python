from django import forms
from .models import Users

class EnromentForm(forms.Form,forms.ModelForm):

    class Meta:
        model = Users
        url = forms.URLField(label='Your website', required=False)
        fields = ('user_name', 'user_phone', 'user_email', 'user_password', 'user_address')