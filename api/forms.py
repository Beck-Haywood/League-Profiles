from django import forms
from api.models import Api

class ApiForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = ['summoner_name']

# class QueryForm(forms.Form):
#     query_name = forms.CharField(max_length=16)
