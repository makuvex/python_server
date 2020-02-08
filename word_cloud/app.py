from konlpy.tag import Kkma
from konlpy.utils import pprint
from pylog import PyLog
import time

'''
requirement
- Install dependencies: sudo apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl
- Install KoNLPy:   $ python3 -m pip install --upgrade pip
                    $ python3 -m pip install konlpy
- MeCab 설치하기 (선택사항): $ sudo apt-get install curl git
                          $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
'''

if __name__ == '__main__':
    before = time.time()
    log = PyLog()
    log = log.setHandler("WARNING")
    log.warning('@@@ start @@@')
    kkma = Kkma()
    #pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
    #pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
    pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
    
    print('diff %s'%(time.time() - before))
    log.warning('@@@ end @@@')
    