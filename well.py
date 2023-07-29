import numpy as np
from chaco.shell import *
import urllib2
import json
from urllib.parse import quote

PV ='CBM:STS:1:1:TEMP'
start_date = '2012-09-27T08%3A00%3A00.000Z'
end_date = '2012-09-28T08%3A00%3A00.000Z'

encoded_start_date = quote(start_date)
encoded_end_date = quote(end_date)
encoded_PV = quote(PV)

req = urllib2.urlopen("http://archiver.slac.stanford.edu/retrieval/data/getData.csv?pv={encoded_PV}&from={encoded_start_date}}&to={encoded_end_date}")
print(req)
data = json.load(req)
secs = [x['secs'] for x in data[0]['data']]
vals = [x['val'] for x in data[0]['data']]
plot(secs, vals, "r-")
xscale('time')
show()