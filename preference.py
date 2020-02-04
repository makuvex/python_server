import os
import sys

class preference:
    host = 'localhost'
    db_name = 'uhan'
    table_name = 'dispensary'
    user = 'makuvex7'
    passwd = 'malice77'
    db_path = os.path.abspath(os.path.dirname(__file__)) + '/db'
    crawling_url = 'http://www.mohw.go.kr/react/popup_200128.html'
    
