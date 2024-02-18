import json
from pprint import pprint
# dn, description, speed, mtu

with open('sample.json', encoding='utf8') as json_fi:
    data = json.load(json_fi)['imdata']
    print('=' * 97)
    print('DN'.ljust(50), 'Description'.ljust(20), 'Speed'.ljust(10), 'MTU'.ljust(10))
    print('-' * 50, '-' * 20, '-' * 10, '-' * 10)
    
    for line in data:
        line = line['l1PhysIf']['attributes']
        line_dn = line['dn']
        line_speed = line['speed']
        line_mtu = line['mtu']
        descr = line['descr']
        print(line_dn.ljust(50), descr.ljust(20), line_speed.ljust(10), line_mtu.ljust(10))