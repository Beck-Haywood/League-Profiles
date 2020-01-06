from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    region = 'na'
    #summonerName = request.args.get('query')
    summonerName = 'NoelPi'
    api = 'RGAPI-ff3bc0da-95fb-456d-85fd-64ffe7b52623'
    params = {
            "region": region,
            "summonerName": summonerName,
            "APIKey": api
        }
    responseJSON_1 = requests.get("https://" + params.get("region") + "1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + params.get("summonerName") + "?api_key=" + params.get("APIKey")).json()
    summonerID = str(responseJSON_1["id"])

    return render(request, 'home.html', {
        'id': summonerID,
        'name': summonerName,
    })
