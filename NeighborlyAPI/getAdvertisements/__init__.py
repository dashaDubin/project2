import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://myneighborlyapiv1cosmosdb:3R1lODz9uJLArhzlpvYz1Cnll7WGfG8eJ53hY04HxEEh7mmW5PRkFbGmvPZyUzNjY4I8STbM17HIyDV11QFebw==@myneighborlyapiv1cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myneighborlyapiv1cosmosdb@" #os.environ['MyDBConnection']
        client = pymongo.MongoClient(url)
        database = client['neigbourlymongodb']
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

