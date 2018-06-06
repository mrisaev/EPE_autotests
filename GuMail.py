import urllib2
import base64
import json
import requests


'''
def getEmail():
    values = '?f=get_email_address&lang=en'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', None)
    request.add_header('SUBSCR', None)
    try:
        result = urllib2.urlopen(request)
        x = result.read()
        print x
        return x
    except urllib2.HTTPError as e:
        print e.read()
'''


def checkEmail():
    values = '?f=check_email&sec=0&PHPSESSID=90uvte8qs49eqc9k0ur95f5ph6'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', '90uvte8qs49eqc9k0ur95f5ph6')
    try:
        result = urllib2.urlopen(request)
        x = result.read()
        print x
    except urllib2.HTTPError as e:
        print e.read()


'''
def getEmailList():
    values = '?f=get_email_list&offset=0&PHPSESSID=90uvte8qs49eqc9k0ur95f5ph6'
    request = urllib2.Request('http://api.guerrillamail.com/ajax.php' + values)
    request.add_header('User-Agent', 'Mozilla/5.0')
    request.add_header('PHPSESSID', '90uvte8qs49eqc9k0ur95f5ph6')
    try:
        result = urllib2.urlopen(request)
        x = result.read()
        x.encode('utf-8')
    except urllib2.HTTPError as e:
        print e.read()
    y = json.loads(x)
    z = y.get('list')[0]
    print z
'''


def getEmail():
    url = 'http://api.guerrillamail.com/ajax.php?'
    payload = {'f': 'get_email_address', 'lang': 'en'}
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        emailData = response.text
        print emailData
        return json.loads(emailData)
    except requests.HTTPError as e:
        print e.read()


def getEmailList():
    url = 'http://api.guerrillamail.com/ajax.php?'
    payload = {'f': 'get_email_list', 'offset': '0', 'PHPSESSID': sessionid}
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print e.read()
    data = json.loads(response.text)
    return data


sessionData = getEmail()
emailAddr = sessionData.get('email_addr')
sessionid = sessionData.get('sid_token')
emailList = getEmailList()
print emailList

mailObj = emailList.get('list')[0]
print mailObj.get('mail_from').encode('utf-8')
print mailObj.get('mail_subject').encode('utf-8')
print mailObj.get('mail_body').encode('utf-8')


# getEmailList()
# checkEmail()
# getEmail()
