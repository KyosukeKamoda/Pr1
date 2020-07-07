# -*- coding: utf-8 -*-

import urllib.request
import json

# データを web から取ってくる
src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=400040'
f = urllib.request.urlopen(src)
strdat = f.read()
f.close()

# JSON レコードの解析
q = json.loads(strdat)

# とりあえず採ってきたデータのタイトルを表示
print(q['title'])
