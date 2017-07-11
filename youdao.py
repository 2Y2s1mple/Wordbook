import sys
import requests
import os
import json

reload(sys)
sys.setdefaultencoding('utf8')

urlx = 'http://fanyi.youdao.com/openapi.do?keyfrom=shabilewordge&key=2028719340&type=data&doctype=json&version=1.1&q='
url = 'http://fanyi.youdao.com/openapi.do?keyfrom=shabilewordge&key=2028719340&type=data&doctype=xml&version=1.1&q='

wl = ['good', 'delicious', 'fabulous', 'excited']
group_tag = 'CET-6'


base_dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(base_dir, 'output.xml'), 'w')
f.write('<wordbook>')
for word in wl:
	f.write('<item>')
	query = urlx + word
	r = requests.get(query)
	reply = json.loads(r.text)	
	f.write('<word>'+reply['query']+'</word>')
	f.write('<trans><![CDATA['+' '.join(reply['basic']['explains'])+']]></trans>')
	f.write('<phonetic><![CDATA[['+reply['basic']['phonetic']+']]]></phonetic>')
	f.write('<tags>'+group_tag+'</tags><progress>-1</progress>')
	print(reply['basic'])
	f.write('</item>')

f.write('</wordbook>')
f.close()
