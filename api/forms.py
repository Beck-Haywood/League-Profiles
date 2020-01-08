from django import forms
from api.models import Api, Video

class ApiForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = ['summoner_name', 'discord_username_and_tag', 'user']
class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["video_name", "videofile"]


# class QueryForm(forms.Form):
#     query_name = forms.CharField(max_length=16)
