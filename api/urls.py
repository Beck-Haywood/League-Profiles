from django.urls import path

from . import views
from api.views import ApiView, ApiCreate, showvideo, VideoShow

app_name = 'api'
urlpatterns = [
    path('', ApiView.as_view(), name='find'),
    path('verify/', ApiCreate.as_view(), name='verify'),
    path('upload/', views.showvideo, name='upload'),
    path('highlights/', VideoShow.as_view(), name='highlights'),
]
