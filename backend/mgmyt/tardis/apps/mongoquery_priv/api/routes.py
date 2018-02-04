from rest_framework import routers  
from tardis.apps.mongoquery.api.viewsets import CollectionViewSet, JobViewSet


api_router = routers.SimpleRouter()  
api_router.register('collections', CollectionViewSet)
api_router.register('jobs', JobViewSet)
