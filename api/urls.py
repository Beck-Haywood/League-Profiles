from django.urls import path

from . import views
from api.views import ApiView, leader, ApiCreate


app_name = 'api'
urlpatterns = [
    path('', ApiCreate.as_view(), name='home'),
    path('api/', ApiView.as_view(), name='view'),
    path('leaderboards/', views.leader, name='leaderboards'),
    #path('query-name/', views.get_query, name='home'),
    #path('api/', ApiView.as_view(), name='view'),



]
