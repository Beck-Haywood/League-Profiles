from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Api(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, unique=True, related_name='test')
    summoner_name = models.CharField(max_length=16, unique=False)
    discord_username_and_tag = models.CharField(max_length=37, null=True)
    #created = models.DateTimeField(auto_now_add=True, null=True)
    tier = models.CharField(max_length=8, null=True)
    rank = models.CharField(max_length=5, null=True)
    winrate = models.FloatField(null=True)
    total_games = models.IntegerField(null=True)
    # added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
    #     null=True, blank=True, on_delete=models.SET_NULL)
    # def save_model(self, request, obj, form, change):
    #     obj.added_by = request.user
    #     super().save_model(request, obj, form, change)

    def __str__(self):
        return self.summoner_name 

class Video(models.Model):
    video_name= models.CharField(max_length=500, null=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.video_name + ": " + str(self.videofile)



