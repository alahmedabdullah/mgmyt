from django.conf.urls import include, url
from tardis.apps.mongoquery.api.routes import api_router as mongoquery_api_router
from tardis.apps.mongoquery.api import views as api_views
from django.views.generic import TemplateView
#from tardis.apps.mongoquery import views as views
from tardis.apps.mongoquery import views_local as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/v1/', include(mongoquery_api_router.urls)),
    url(r'^api/v1/collections_list/$', api_views.collections_list),
    url(r'^api/v1/collections_list/(?P<collection_name>[\w]+)/$', api_views.collections_list),
    url(r'^api/v1/getquery/(?P<collection_name>[\w]+)/$', api_views.get_query),
    url(r'^(?P<experiment_id>\d+)/$', views.index),
    #url(r'^mongoquery/(?P<experiment_id>\d+)/$', TemplateView.as_view(template_name="index.html"), name='index'),
    #url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
