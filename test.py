from flask import Flask, make_response
from flask_restful import reqparse, abort, Api, Resource
from mySqlService import mySqlService
import json
from urllib.parse import parse_qsl
import requests

if __name__ == '__main__':
    #app.run(debug=True)
    
    url = "https://wuhanvirus.kr/stat.json"
    res = requests.get(url)

    if res.status_code != 200:
        print('[Error] Failed to request: {url}')

    print(res.json())
        
    print(json.dumps(res.json(),ensure_ascii=False, indent=4))
    #r = res.json()
    #json_val = json.dumps(r, c, indent=4)
    #print(json_val)
    #resp = make_response(res.text)
    #pyhtonprint('@@@@ type(%s)'%resp)
    