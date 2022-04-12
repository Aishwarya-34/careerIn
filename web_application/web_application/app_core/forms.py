from django.forms import ModelForm
from django import forms
from web_application.app_core.models import Resume
from django.forms import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#changes my ash
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# till here


class ResumeModelForm(forms.ModelForm):

	class Meta:
		model = Resume
		fields = [
			'pdf',
			'industry'
		]
		widgets = {
		'pdf': ClearableFileInput(attrs = {'multiple': True}),
		}
