from flask_restful import Resource
from flask import request
import os
from pprint import pprint
from google.cloud import storage
from lib2to3.pytree import convert
from markupsafe import escape



#app.config['GOOGLE_APPLICATION_CREDENTIALS'] = r'misonube2022equipo23-8093e2406c0a.json'


#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config['GOOGLE_APPLICATION_CREDENTIALS']

storage_client = storage.Client()
bucket_name = 'bucket_music_file_storage-1'
blob_name = 'upfiles/prueba'
blog_name = 'upfiles/prueba'

#post('upfiles/prueba','Prueba/prueba.json')
#get('upfiles/prueba', 'E:/Desarrollo/Practicas/Universidad/semestre2/Ciclo2/Nube/Desarrollo/DesarrolloCloudMISO/DesarrolloCloudApiConverter/downloaded/prueba.json')

class statusCheck(Resource):
    def get(self):
        return {'status': 'ok'}

class ManageBucket:
    def post(file_path):
            # response = post('/docs/requirementABC', 'requirements.txt', bucket_name)
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_path)
            print('upload')
            return blob

    def get(file_path):
            # get('Voice List', r'H:\PythonVenv\GoogleAI\Cloud Storage\Voice List.csv', bucket_name)
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blog_name)
            with open(file_path, 'wb') as f:
                storage_client.download_blob_to_file(blob, f)
            print('download')