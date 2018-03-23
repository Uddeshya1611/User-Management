from django import forms

from .models import Gruser

class Signup(forms.ModelForm):

	class Meta:
		model = Gruser
		fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'gender')
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(Signup, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)

class Login(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)