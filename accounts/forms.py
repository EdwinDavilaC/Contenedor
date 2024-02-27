from django import forms
from accounts.models import Usuario



class UserForm(forms.ModelForm):

    class Meta:

        model = Usuario
        fields = '__all__'
        
