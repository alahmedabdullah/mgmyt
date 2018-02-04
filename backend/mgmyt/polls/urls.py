from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from . import views

#1----------------
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

#2----------------before_less_code_is_better---------------
urlpatterns = [
     #url('^', include('django.contrib.auth.urls'))

     #url(r'^accounts/login/$', auth_views.login, {'template_name':'polls/registration/login.html'}, name='my_login'),

     # "ex: /polls/index/"
     url(r'^$', views.index, name='index'),

     # "ex: /polls/5/"
     url(r'^/testdetail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

     # "ex: /polls/5/results/"
     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

     # "ex: /polls/5/vote/"
     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#3----------------less_code_is_better---------------
#urlpatterns = [
#    url(r'^/$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#]
