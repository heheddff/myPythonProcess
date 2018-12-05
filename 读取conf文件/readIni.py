import configparser
import string, os, sys
import zipfile
import re

cf = configparser.ConfigParser()
 
cf.read("zipConfig.conf")
 
 
#read by type
db_host = cf.get("global", "logType")
db_port = cf.get("global", "srcDir")
db_user = cf.get("global", "bakDir")
db_pass = cf.getint("global", "number")
 
print("db_host:", db_host.split(','))
print("db_port:", db_port)
print("db_user:", db_user)
print("db_pass:", type(db_pass))

p = "172.20.68.*"
if re.search(p,"172.20.38.20"):
    print(re.search(p,"172.20.68.20"))
