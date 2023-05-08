"""in this code i am trying to get a systematic way to get the data from clients to csv formatt"""

"hera pheri"

import csv
import time
import random

samples = {"place":[{'data': random.randint(1,10), 'time': time.time()}]*5}


with open('new.csv', 'w') as f:
        fieldnames = ['data','time']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        
        thewriter.writeheader()
        for key, value in samples.items():
            print(key)
            for val in value:
                packet = {'data':val['data'],
                        'time':val['time']
                        }
                print(packet)
                thewriter.writerow(packet)