from django import forms

from .models import Signup

class ContactForm(forms.Form):
	fullname = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ['email','fullname']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_fullname(self):
		fullname = self.cleaned_data.get('fullname')
		return fullname