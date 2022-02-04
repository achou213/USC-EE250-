#sample code to read in and process a json file
import sys
import json

jt = open(sys.argv[1], "r").read()

jd = json.loads(jt)
print(type(jd))
print(jd.keys())

#code here to further manipulate the python dictionary as needed
#print(jd['data'][0]['city_name'])



