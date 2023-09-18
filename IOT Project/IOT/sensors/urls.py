from django.urls import path
from . import views

urlpatterns = [
    path('postsensorData/',views.postsensorData.as_view()),#create
    path('getsensorData/',views.getsensorData.as_view()), #fetach all
    #fetchparticlarsensorByID
    path('getsensorData/<sensorid>/',views.getsensorDataDetails.as_view()),
    #update
    path('updatesensorData/',views.updatesensorData.as_view()),
    #delete
    path('deletesensorData/<sensor_id>/',views.deletesensorData.as_view()),
    #notification
    path('notifyUser/',views.notifyUser.as_view()),

]