from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
import requests
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from api.models import Api, Video
from api.forms import ApiForm, VideoForm

def showvideo(request):

    #lastvideo = Video.objects.last()

    #videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context= {#'videofile': videofile,
              'form': form
              }
    return render(request, 'videos.html', context)

class VideoShow(ListView):
    template_name = 'highlights.html'
    model = Video
    def get(self, request):
        """ GET a list of Videos. """
        videos = Video.objects.all()

        return render(request, self.template_name, {
           'videos': videos,
        })
    

class ApiCreate(CreateView):
  template_name = 'verify.html'
  form_class = ApiForm
  success_url = '' 

  def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save(commit = False)
    return HttpResponseRedirect(self.get_success_url())

  def post(self, request):

    if request.method == 'POST':
        form = ApiForm(request.POST)
        region = 'na'
        summonerName = form.data['summoner_name']
        api = 'RGAPI-2329b1b5-fdad-4792-b7cc-8862b0c21d9b'

        params = {
            "region": region,
            "summonerName": summonerName,
            "APIKey": api
        }

        responseJSON_1 = requests.get("https://" + params.get("region") + "1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + params.get("summonerName") + "?api_key=" + params.get("APIKey")).json()
        summonerID = str(responseJSON_1["id"])
        #level =  str(responseJSON_1['summonerLevel'])
        responseJSON_2 = requests.get("https://" + params.get("region") + "1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + params.get("APIKey")).json()


        if responseJSON_2[0]["queueType"] == "RANKED_SOLO_5x5":
            infoNum = 0
        elif responseJSON_2[0]["queueType"] == "RANKED_SOLO_5x5":
            infoNum = 1
        else:
            infoNum = 2
        
        tier = responseJSON_2[infoNum]["tier"].lower().capitalize()
        rank = responseJSON_2[infoNum]["rank"]
        wins = str(responseJSON_2[infoNum]["wins"])
        losses = str(responseJSON_2[infoNum]["losses"])

        winrate_dec = responseJSON_2[infoNum]["wins"]/(responseJSON_2[infoNum]["wins"] + responseJSON_2[infoNum]["losses"])
        winrate = str(round(winrate_dec * 100, 2))

        total_games = (int(wins) + int(losses))

        form.data._mutable = True
        form.instance.tier = tier
        form.instance.rank = rank
        form.instance.winrate = winrate
        form.instance.total_games = total_games
        form.save()
        
        return HttpResponseRedirect('api/')
    return render(request, self.template_name, {'form': form})

class ApiView(ListView):
    model = Api
    template_name = 'find.html'

    def get(self, request):
        """ GET a list of Info. """
        apis = Api.objects.all()

        return render(request, self.template_name, {
           'apis': apis,
        })
