from django.shortcuts import render, HttpResponseRedirect
import requests
from django.views.generic import CreateView
from django.views.generic import ListView
from api.models import Api, Video
from api.forms import ApiForm, VideoForm
from dotenv import load_dotenv
import os

def showvideo(request):

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
  
    #print('Non Errors:', form_post.non_field_errors())

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit = False)
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request):
        if request.method == 'POST':
            form = ApiForm(request.POST)
            region = 'na'
            summonerName = form.data['summoner_name']
            load_dotenv()
            api = str(os.getenv('API_CODE'))
            api = 'RGAPI-1f3392e9-1c3b-4dda-bf33-2a3d37c11dd3'

            params = {
                "region": region,
                "summonerName": summonerName,
                "APIKey": api
            }

            responseJSON_1 = requests.get("https://" + params.get("region") + "1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + params.get("summonerName") + "?api_key=" + params.get("APIKey")).json()
            summonerID = str(responseJSON_1["id"])
            responseJSON_2 = requests.get("https://" + params.get("region") + "1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + params.get("APIKey")).json()


            if responseJSON_2[0]["queueType"] == "RANKED_SOLO_5x5":
                infoNum = 0
            elif responseJSON_2[1]["queueType"] == "RANKED_SOLO_5x5":
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
            #form.save_m2m()
            #form.save()
            form.instance.summoner_name = summonerName
            form.instance.save()


            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

class ApiView(ListView):
    model = Api
    template_name = 'find.html'

    def get(self, request):
        """ GET a list of Info. """
        apis = Api.objects.all()
        #api = Api.objects.first()
        #print(api.added_by)
        #print(api.user.username)

        return render(request, self.template_name, {
           'apis': apis,
        })
