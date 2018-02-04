import ast
from pymongo import MongoClient
from bson.json_util import dumps
import logging
import time
logger = logging.getLogger(__name__)
print __name__

def mdb_get_colnm_conuri_dict(colobject):
    pass

def mdb_get_mongo_rowcount(clcobj,mongo_uri):
    mongo_dbname= clcobj.database_name
    mongo_collection = clcobj.collection_name
    #mongo_uri = rdb_get_mongo_uri(clcobj)
    db = MongoClient(mongo_uri)[mongo_dbname]
    collection = db[mongo_collection]
    #rowcount = collection.count()
    rowcount = pymongo_count(collection)
    return rowcount
   
def mdb_query_mongodata(query_text,colobject):
    if not colobject:
        logger.debug('Collection : "%s" does not exist' %colobject.collection_name)
        return []
    db_name= colobject.database_name
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

    db = MongoClient(uri)[colobject.database_name]
    collection = db[colobject.collection_name]
    logger.debug('Collection Name : "%s", Dtabase_name: "%s" Uri: "%s"' %(colobject.collection_name,colobject.database_name,uri))

    query_dict = ast.literal_eval(query_text)
    logger.debug('Query Text : %s' %query_dict)

    #mongo_result = collection.find(query_dict)
    mongo_result = pymongo_find(collection, query_dict, colobject.collection_querylimit)
    mongo_result_list=[]
    for mr in mongo_result:
       mr_dump = dumps(mr)
       mongo_result_list.append(mr_dump)
       logger.debug('%s' %mr_dump)
    return mongo_result_list

def mdb_run_job(job_object):
    mongo_uri = job_object.collection.collection_uri
    mongo_querylimit = job_object.collection.collection_querylimit
    mongo_db = MongoClient(mongo_uri)[job_object.collection.database_name]
    mongo_collection = mongo_db[job_object.collection.collection_name]
    #mongo_result = mongo_collection.find(job_object.query_text)
    mongo_result = pymongo_find(mongo_collection, job_object.query_text, mongo_querylimit)
    mongo_result_list=[]
    for mr in mongo_result:
       mr_dump = dumps(mr)
       mongo_result_list.append(mr_dump)
       logger.debug('%s' %mr_dump)
    #time.sleep(10)
    return mongo_result_list

def pymongo_find(mongo_collection, mongo_query, query_limit=0):
    if query_limit == 0:
        return mongo_collection.find(mongo_query)
    elif query_limit > 0:
        return mongo_collection.find(mongo_query, limit=query_limit)
    else:
        return None
    
def pymongo_count(mongo_collection, maxTime=0):
    if maxTime == 0:
        return mongo_collection.count()
    elif maxTime > 0:
        return mongo_collection.count(maxTimeMS=maxTime)
