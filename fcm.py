import requests
import json
from constant import FCMConstant

'''
requirements pip
- requests
'''

def send_to_token(fcm_token, title, body, extra):
    auth = 'key='+FCMConstant.fcm_server_key
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Charset': 'UTF-8'
    }
    content = {
        'to': fcm_token,
        'data': {
            'title': title,
            'body': body,
            'extra': extra
        },
        'notification': {
            'sound' : 'default',
            'title': title,
            'body': body,
            'extra': extra,
            'content_available': True
        },
        "priority": "high"
    }
    
    response = requests.post(FCMConstant.fcm_url, data = json.dumps(content), headers=headers)
    print('fcm send response %s, content %s'%(response,content))


if __name__ == '__main__':
    #send_to_token(Constant.fcm_test_token, '테스트 타이틀', '테스트 바디', 'https://www.daum.net')
    topic = 'asdf'
    send_to_token(f'/topics/{topic}', '토픽 테스트 타이틀', '토픽 테스트 바디', 'https://www.daum.net')


    