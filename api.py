from flask import Flask, make_response
from flask_restful import reqparse, abort, Api, Resource
from mySqlService import mySqlService
import json
from urllib.parse import parse_qsl
import requests

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
#parser.add_argument('task')

class Dispensary(Resource):
    def get(self):
        sqlService = mySqlService()
        resp = make_response(json.dumps(sqlService.selectAllToJson(), ensure_ascii=False, indent=4))
        return resp

class Summary(Resource):
     def get(self):
        url = "https://wuhanvirus.kr/stat.json"
        res = requests.get(url)

        if res.status_code != 200:
            print('[Error] Failed to request: {url}')
            return {
                'code' : '0',
                'result' : null
            }

        r = {'code' : '200', 'result' : res.json()}
        return make_response(json.dumps(r, ensure_ascii=False, indent=4))
    
api.add_resource(Dispensary, '/dispensary')
api.add_resource(Summary, '/summary')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
