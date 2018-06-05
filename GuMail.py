import ssl
import urllib2
import base64
import json


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getEmail():
    values = '?f=get_email_address&lang=en'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', None)
    request.add_header('SUBSCR', None)
    try:
        result = urllib2.urlopen(request, context=ctx)
        x = result.read()
        print x
    except urllib2.HTTPError as e:
        print e.read()

def checkEmail():
    values = '?f=check_email&sec=0&PHPSESSID=ke188oenqd74o96osnulh6gql3'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', 'ke188oenqd74o96osnulh6gql3')
    try:
        result = urllib2.urlopen(request, context=ctx)
        x = result.read()
        print x
    except urllib2.HTTPError as e:
        print e.read()

def getEmailList():
    values = '?f=get_email_list&offset=0&PHPSESSID=ke188oenqd74o96osnulh6gql3'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', 'ke188oenqd74o96osnulh6gql3')
    try:
        result = urllib2.urlopen(request, context=ctx)
        x = result.read()
        x.encode('utf-8')
    except urllib2.HTTPError as e:
        print e.read()
    y = json.loads(x)
    z = y.get('list')[0]
    print z


getEmailList()
checkEmail()
#getEmail()
