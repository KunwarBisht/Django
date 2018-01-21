from django.conf.urls import url
from . import views 

urlpatterns= [
    url(r'^$',views.index, name='index')]  ##views =page ; index =fuction
    #r=regular expression;  ^ =start ,$ =end
