from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Task






class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control','id':'nameid1'}),
			'email': forms.TextInput(attrs={'class':'form-control','id':'nameid2'}),
			'password1': forms.TextInput(attrs={'class':'form-control','id':'nameid3'}),
			'password2': forms.TextInput(attrs={'class':'form-control','id':'nameid4'}),
			}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	




class DateInput(forms.DateInput):
    input_type = 'date'


class CreateTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title','description','start_date','end_date']
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control','id':'titleid'}),
			'description': forms.Textarea(attrs={'class':'form-control','id':'desid'}),
            'start_date': DateInput(attrs={'type': 'date','id':'startid'}),
            'end_date': DateInput(attrs={'type': 'date','id':'endid'}),
        }
		exclude = ['user',]