import requests
from pprint import pprint

import sys
sys.path.append('.')

with open('/home/yuhui/Project/defect_concoct/test/test.json') as fid:
    input_string = ''.join(fid.readlines()).replace('\n', '')

data = dict()
data['headers'] = dict(
    input_string = input_string
)

resp = requests.post(
    url='http://127.0.0.1:3700/infer/',
    **data
)

pprint(resp.json())