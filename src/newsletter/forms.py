from django import forms

from .models import Signup
from .models import Contact
from .models import BookBearLetter

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['fullname','phone_number','email','message']
		widgets={
		 	"fullname":forms.TextInput(attrs={'placeholder':'Fullname'}),
		 	"phone_number":forms.TextInput(attrs={'placeholder':'Phone Number'}),
		 	"email":forms.TextInput(attrs={'placeholder':'Email'}),
		 	"message":forms.Textarea(attrs={'placeholder':'Message'}),
		 	}

class BookBearLetterForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['fullname','email','message']
		widgets={
		 	"fullname":forms.TextInput(attrs={'placeholder':'Fullname'}),
		 	"email":forms.TextInput(attrs={'placeholder':'Email'}),
		 	"message":forms.Textarea(attrs={'placeholder':'Message'}),
		 	}  

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