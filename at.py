from selenium import webdriver
import requests
import xml.etree.ElementTree as ET
import time
import urllib2
import ssl
import random
import json

driver = webdriver.Firefox()
driver.get("https://exonum.com/demo/voting/")


'''
def getWikiText(link):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib2.urlopen(link, context=ctx)
    plainHTML = html.read()
    tree = ET.parse(plainHTML)
    root = tree.getroot()
    result = root.find('r').text
    print result.encode('utf-8')
'''


def getToCandidates():
    driver.get("https://exonum.com/demo/voting/")
    btn1 = driver.find_element_by_css_selector(
        "div[class='button button-red']")
    btn1.click()
    time.sleep(2)
    checker = driver.find_element_by_xpath(
        '//td[text()="Estonian Presidential Election"]')
    checker.click()
    time.sleep(1)
    btn2 = driver.find_element_by_xpath('//div[text()="VOTE IN ELECTION"]')
    btn2.click()
    time.sleep(2)
    nameElemList = driver.find_elements_by_xpath('//td[@class="ng-binding"]')
    return nameElemList
    time.sleep(2)


def valLinks(nameIndex):
    nameElemList = driver.find_elements_by_xpath('//td[@class="ng-binding"]')
    nameElemList[nameIndex].click()
    time.sleep(1)
    linkElem = driver.find_element_by_xpath(
        '//a[@class="list-option-link"]')
    link = linkElem.get_attribute('href')
    name = nameElemList[nameIndex].text.encode('utf-8')
    print linkElem.get_attribute('href')
    print nameElemList[nameIndex].text.encode('utf-8')
    if link[0:24] == 'https://en.wikipedia.org' and name.replace(' ', '_') in link:
        print 'Passed'
    else:
        print 'Failed'
    time.sleep(2)


def vote():
    btn3 = driver.find_element_by_xpath('//div[text()="VOTE IN ELECTION"]')
    btn3.click()
    time.sleep(1)
    btn4 = driver.find_element_by_xpath('//div[text()="YES"]')
    btn4.click()
    time.sleep(1)
    memoElem = driver.find_element_by_css_selector(
        'div[class="code-box code-box-bigger ng-scope ng-binding"]')
    memo = memoElem.text.encode('utf-8')
    bHashElem = driver.find_element_by_css_selector(
        'div[class="code-box ng-scope ng-binding"]')
    bHash = bHashElem.text.encode('utf-8')
    print memo
    print bHash
    btnSign = driver.find_element_by_css_selector(
        'div[ng-click="signModal()"]')
    btnSign.location_once_scrolled_into_view
    time.sleep(1)
    btnSign.click()
    time.sleep(1)
    digits = driver.find_elements_by_css_selector(
        'div[class="keyboard-button-digit"]')
    for i in xrange(4):
        print random.randint(0, 9)
        digit = random.randint(0, 9)
        btn5 = digits[digit]
        btn5.click()
        time.sleep(1)
    btnSignBlt = driver.find_element_by_css_selector(
        'div[ng-click="submitSign()"]')
    btnSignBlt.click()
    time.sleep(2)
    return [memo, bHash]


def sendBallot(emailAddr):
    inpField = driver.find_element_by_css_selector(
        'input[ng-model="inputs.email"]')
    inpField.send_keys(emailAddr)
    submitBlt = driver.find_element_by_xpath('//div[text()="SUBMIT BALLOT"]')
    submitBlt.click()
    time.sleep(2)


def getEmail():
    url = 'http://api.guerrillamail.com/ajax.php?'
    payload = {'f': 'get_email_address', 'lang': 'en'}
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        sessionData = json.loads(response.text)
        print sessionData
        return sessionData
    except requests.HTTPError as e:
        print e.read()


def getEmailList(sessionId):
    url = 'http://api.guerrillamail.com/ajax.php?'
    payload = {'f': 'get_email_list', 'offset': '0', 'PHPSESSID': sessionId}
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print e.read()
    data = json.loads(response.text)
    return data


def valEmailData(emailData, sessionId):
    emailList = getEmailList(sessionId)
    print emailList

    mailObj = emailList.get('list')[0]
    mailFrom = mailObj.get('mail_from').encode('utf-8')
    mailSubject = mailObj.get('mail_subject').encode('utf-8')
    mailBody = mailObj.get('mail_body').encode('utf-8')
    print mailObj.get('mail_from').encode('utf-8')
    print mailObj.get('mail_subject').encode('utf-8')
    print mailObj.get('mail_body').encode('utf-8')
    print emailData
    '''
    if mailFrom == 'voting2016app@gmail.com':
        print 'sender is valid'
    else:
        print 'sender is INVALID!'
    if mailSubject == 'Voter, your ballot has been successfully posted on public bulletin board':
        print 'subject is valid'
    else:
        print 'subject is INVALID!'
    if emailData[0] in mailBody and emailData[1] in mailBody:
        print 'hash and MEMO are valid'
    else:
        print 'hash or/and MEMO are INVALID!'
    '''


credentials = getEmail()
emailAddr = credentials.get('email_addr')
print emailAddr
sessionId = credentials.get('sid_token')
nameElemList = getToCandidates()
for i in range(len(nameElemList)):
    getToCandidates()
    valLinks(i)
    emailData = vote()
    sendBallot(emailAddr)
    time.sleep(5)
    valEmailData(emailData, sessionId)


driver.close()
