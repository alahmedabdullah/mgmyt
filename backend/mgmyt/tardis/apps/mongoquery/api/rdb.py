from django.core.exceptions import ObjectDoesNotExist
from tardis.apps.mongoquery.models import Collection, UserCollection, Job  
from .mdb import mdb_get_mongo_rowcount 
from bson.json_util import dumps
from collections import defaultdict
import time

import logging
logger = logging.getLogger(__name__)
print __name__

def rdb_get_clcname_clcdesc_dict(collection_details,all_clcobjects):
    for colls in all_clcobjects:
        collection_details[colls.collection_name] =  {}
        collection_details[colls.collection_name]['description'] = colls.collection_description
        collection_details[colls.collection_name]['rowcount'] = 'N'
        collection_details[colls.collection_name]['link'] = 'N'
    return collection_details

def rdb_get_clcname_clcdesc_dict2(collection_details,all_clcobjects):
    for colls in all_clcobjects:
        collection_details[colls.collection_name] =  {}
        collection_details[colls.collection_name]['description'] = colls.collection_description
    return collection_details

def rdb_get_clcname_clclink_dict(collection_details,tusr_clcobjects):
    for colls in tusr_clcobjects:
        collection_details[colls.collection_name]['link'] = 'Y'
    return collection_details

def rdb_get_clcname_rowcount_dict(collection_details,all_clcobjects):
    for colls in all_clcobjects:
        rowcount = rdb_get_mongo_rowcount(colls)
        collection_details[colls.collection_name]['rowcount'] = rowcount
    logger.debug('Collections Distionary: %s' %collection_details)
    return collection_details

def rdb_get_clcname_rowcount(all_clcobjects):
    for colls in all_clcobjects:
        rowcount = rdb_get_mongo_rowcount(colls)
        #time.sleep(10)
    return True

def rdb_get_clcname_rowcount_one(clcobject):
    rowcount = rdb_get_mongo_rowcount(clcobject)
    logger.debug('Collection rowcount: %s' %rowcount)
    #time.sleep(10)
    return True

def rdb_set_clcname_clclink(all_collection_objects,tardisuser_collection_objects):
    for aco in all_collection_objects:
        aco.collection_querylink = 'N'
        aco.save(update_fields=['collection_querylink'])

    for aco in all_collection_objects:
        for tuco in tardisuser_collection_objects:
            if tuco.collection_name == aco.collection_name:
                aco.collection_querylink = 'Y'
                aco.save(update_fields=['collection_querylink'])
    return True

def rdb_get_clcname_querylink_dict(all_collection_objects,tardisuser_collection_objects):
    collections_querylink=[]
    for aco in all_collection_objects:
        temp_dict={}
        temp_dict['collection_name'] = aco.collection_name
        temp_dict['collection_querylink'] = 'N'
        collections_querylink.append(temp_dict.copy())


    for list_item in collections_querylink:
        for tuco in tardisuser_collection_objects:
            if tuco.collection_name == list_item['collection_name']:
                list_item['collection_querylink'] = 'Y'
            
    logger.debug('collections_querylink list: %s' %(collections_querylink))
    return collections_querylink

def rdb_get_clcname_clcuri_dict(all_clcobjects):
    collection_details={}

    for clcobj in all_clcobjects:
        db_name= clcobj.database_name
        host_name= str(clcobj.host_name)
        port_number=str(clcobj.port_number)
        user_name=clcobj.collection_user
        user_password=clcobj.collection_pass
        authsource_database=clcobj.authsource_database

        uri= "mongodb://" \
              + user_name + ":" + user_password \
              + "@" \
              + host_name + ":" + port_number \
              + "/?authSource=" + authsource_database
        logger.debug('URI : %s' %uri)
        #uri= "mongodb://" \
        #      + host_name + ":" + port_number \

        collection_details[clcobj.collection_name] = uri
        logger.debug('Collections: %s %s' %(colls.collection_name,uri))

    return collection_details

def rdb_get_tardisuser_collection_objects(tardisuser_object):
    try:
        theCollectionObjects = tardisuser_object.collection.all()
    except ObjectDoesNotExist as e:
        theCollectionObjects = None
    logger.debug('Tardisuser UserCollection Objects: %s' %theCollectionObjects)
    return theCollectionObjects

def rdb_get_all_collection_objects():
    try:
        allCollectionObjects = Collection.objects.all()
    except ObjectDoesNotExist as e:
        allCollectionObjects = None
    logger.debug('All Collection Objects: %s' %allCollectionObjects)
    return allCollectionObjects

def rdb_get_mongo_rowcount(colobject):
    if not colobject.collection_rowcount:
        uri = rdb_get_mongo_uri(colobject)
        rowcount = mdb_get_mongo_rowcount(colobject, uri)
        colobject.collection_rowcount = rowcount
        colobject.save(update_fields=['collection_rowcount'])
        logger.debug('Setting mongo rowcount in %s : %s' %(colobject.collection_name, rowcount))
        return colobject.collection_rowcount
    else:
        return colobject.collection_rowcount

def rdb_get_mongo_uri(colobject):
    if not colobject.collection_uri:
        return rdb_set_mongo_uri(colobject)
    else:
        return colobject.collection_uri
   
def rdb_set_mongo_uri(colobject):
    host_name= str(colobject.host_name)
    port_number=str(colobject.port_number)
    user_name=colobject.collection_user
    user_password=colobject.collection_pass
    authsource_database=colobject.authsource_database

    uri= "mongodb://" \
          + user_name + ":" + user_password \
          + "@" \
          + host_name + ":" + port_number \
          + "/?authSource=" + authsource_database
    colobject.collection_uri = uri
    colobject.save(update_fields=['collection_uri'])
    logger.debug('Setting mongo rowcount in %s : %s' %(colobject.collection_name, uri))
    return uri

def rdb_initiate_job(collection_object,qdict):
    job_object = Job(query_text=qdict,status='N',collection=collection_object)
    job_object.save()
    context = { "job_id" : job_object.id,
                "collection_name" : job_object.collection.collection_name,
                "query_text" : job_object.query_text,
                "job_status" : job_object.status,
              } 
    logger.debug('Job object:  %s' %context)
    return job_object 

#def rdb_populate_mongo_result(mongo_result_raw, job_object):
#    for tr in mongo_result_raw:
#        tr_dump = dumps(tr)
#        mongoresult_object = MongoResult(mongo_result=tr_dump,job=job_object)
#        mongoresult_object.save()
#        logger.debug('%s' %tr_dump)
#
#    job_object.status = 'S'
#    job_object.save(update_fields=['status'])
#    return job_object

#def rdb_get_mongo_result(job_object):
#    mongo_result = job_object.mongoresult_set.all()
#    logger.debug('%s' %mongo_result)
#    return mongo_result

def dump_dict(the_dict):
    the_list=[]
    for dict_item in the_dict:
       dict_item_dump = dumps(dict_item)
       the_list.append(dict_item_dump)
    logger.debug('The dump list: %s' %the_list)
    return the_list

