from exceptions import TypeError, SyntaxError, ValueError
from tardis.apps.mongoquery.models import Collection, UserCollection, Job  
from tardis.apps.mongoquery.api.serializers import CollectionSerializer, JobSerializer
from tardis.apps.mongoquery.forms import QueryForm
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer 
from django.shortcuts import get_object_or_404
from .rdb import *
from .mdb import *
import json

import logging
logger = logging.getLogger(__name__)
print __name__

@login_required
@renderer_classes((JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer))
@api_view(['GET'])
def collections_list(request,collection_name=None,format=None):
    tardisuser = request.user
    #tardisuser = "myt"
    if  not collection_name:
        tardisuser_object = get_object_or_404(UserCollection,tardis_user=tardisuser)
        tardisuser_collection_objects = tardisuser_object.collection.all()
        all_collection_objects = Collection.objects.all()

        #rdb_set_clcname_clclink(all_collection_objects,tardisuser_collection_objects)
        collections_querylink = rdb_get_clcname_querylink_dict(all_collection_objects,tardisuser_collection_objects)

        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections,fields=('collection_name','collection_description'), many=True)

        return Response({ 'collections_list' : serializer.data, 'collections_querylink' : collections_querylink } )

    elif collection_name:
        logger.debug("Collection name: %s" %collection_name)
        collection_object = Collection.objects.get(collection_name=collection_name)
        logger.debug("Collection object: %s" %collection_object)
        rdb_get_clcname_rowcount_one(collection_object)

        collections = Collection.objects.get(collection_name=collection_name)
        logger.debug("Collections : %s" %collections)
        serializer = CollectionSerializer(collections,fields=('collection_name','collection_rowcount'))

        return Response(serializer.data)

@login_required
@renderer_classes((JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer))
@api_view(['GET','POST'])
def get_query(request,collection_name, format=None):
    tardisuser = request.user
    #tardisuser = "myt"
    logger.debug("Collection : %s" %collection_name)
    logger.debug("Method : %s" %request.method)
    logger.debug("Data : %s" %request.data)

    template_name = 'mongoquery.html'
    mongo_result={}
    queryform = QueryForm()
    collection_object = get_object_or_404(Collection,collection_name=collection_name)
    mongo_uri = rdb_get_mongo_uri(collection_object)
    mongo_db = MongoClient(mongo_uri)[collection_object.database_name]
    mongo_collection = mongo_db[collection_object.collection_name]
     
    if request.method == 'POST':
        queryform = QueryForm(request.data)
        if queryform.is_valid():
            query_text = (queryform.cleaned_data['query_text']).strip()
            try:
               query_dict = ast.literal_eval(query_text)
            except  SyntaxError as e:
                logger.debug("SyntaxError : %s" %str(e))
                return Response({'mongo_result': {str(e)}, 'collection_name': collection_name})
            except  ValueError as e:
                logger.debug("ValueError : %s" %str(e))
            except  TypeError as e:
                logger.debug("TypeError : %s" %str(e))

            query_text = query_dict

        job_object = rdb_initiate_job(collection_object,query_dict)
        mongo_result = mdb_run_job(job_object)

        #job_object = rdb_populate_mongo_result(mongo_result_raw, job_object)
        #mongo_result= rdb_get_mongo_result(job_object)


        return Response({'mongo_result': mongo_result, 'collection_name': collection_name})

    elif request.method == 'GET':
        return Response({'collection_name': collection_name})
