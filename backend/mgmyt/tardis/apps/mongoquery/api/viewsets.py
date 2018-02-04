from rest_framework import viewsets  
from rest_framework.decorators import detail_route
from tardis.apps.mongoquery.models import Collection, Job  
from tardis.apps.mongoquery.api.serializers import CollectionSerializer, JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)
print __name__

class CollectionViewSet(viewsets.ModelViewSet):  
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class JobViewSet(viewsets.ModelViewSet):  
    queryset = Job.objects.all()
    serializer_class = JobSerializer

#@login_required
#@renderer_classes((JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer))
@api_view(['GET'])
def collections_list(request):
    tardisuser = request.user
    tardisuser_object = get_object_or_404(UserCollection,tardis_user=tardisuser)
    tardisuser_collection_objects = tardisuser_object.collection.all()
    all_collection_objects = Collection.objects.all()
    for aco in all_collection_objects:
        for tuco in tardisuser_collection_objects:
            if aco.collection_name == tuco.collection_name:
                aco.collection_querylink = 'Y'
            else:
                aco.collection_querylink = 'N'
        aco.save(update_fields=['collection_querylink'])
    
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)
