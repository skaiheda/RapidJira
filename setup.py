import requests
import sys, os, re, json
import socket
import requests
import requests.packages.urllib3
import ssl
import re
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time

nexpose = 'https://some_url:[portNumber]/api/3'
jira = 'https://some_url/rest/api/2/issue'

username = 'safarovaas'
print("Enter your ldap password: ")
password=input()

headers = {
    'Content-Type': 'application/json',
}

#remove ssl error and security warning
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

urllib3.disable_warnings(InsecureRequestWarning)
