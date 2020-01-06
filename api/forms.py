from django import forms
from api.models import Api

class ApiForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = '__all__'