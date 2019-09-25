from django import forms
from .models import Users

class EnromentForm(forms.Form,forms.ModelForm):

	url = forms.URLField(label='Your website', required=False)

	class Meta:
		model = Users
		fields = ('user_name', 'user_phone', 'user_email', 'user_password', 'user_address')