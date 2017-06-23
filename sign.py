# coding=UTF-8
#!/usr/bin/env python
__author__ = 'witon_an'

import hashlib
import hmac
import datetime
import urllib

import time
def signature(str,key):
    return hmac.new(key,str,hashlib.sha1).digest().encode('base64').rstrip()


def url_encode(str):
    temp = {"1":str};
    temp = urllib.urlencode(temp)[2:];
    return temp.replace("+","%20").replace("*", "%2A").replace("%7E", "~")

#获取UTC时间的字符串
def getTimeUTC():
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ";
    tt = time.time();
    return datetime.datetime.utcfromtimestamp(tt).strftime(UTC_FORMAT);

def getURLWithPara(para):
    parameters= sorted(para.iteritems(), key=lambda d:d[0]);
    str = "";
    for p in parameters:
        str = str +"&"+ url_encode(p[0]) + "=" + url_encode(p[1]);
    return str[1:];

def getSign(para,key):
    str = "GET&"+ url_encode("/")+"&"+url_encode(getURLWithPara(para));
    return  url_encode(signature(str,key+"&"));


# parameters = {};
# parameters["Action"] = "DescribeDomainRecords";
# parameters["DomainName"] = "example.com";
# parameters["Version"] = "2015-01-09";
# parameters["AccessKeyId"] = "testid";
# parameters["Timestamp"] = "2016-03-24T16:41:54Z";
# parameters["SignatureMethod"] = "HMAC-SHA1";
# parameters["SignatureVersion"] = "1.0";
# parameters["SignatureNonce"] = "f59ed6a9-83fc-473b-9cc6-99c95df3856e";
# parameters["Format"] = "XML";

# print(parameters)
# parameters= sorted(parameters.iteritems(), key=lambda d:d[0])
#
# str = "";
# for p in parameters:
#     str = str +"&"+ url_encode(p[0]) + "=" + url_encode(p[1])
# str = "GET&"+ url_encode("/")+"&"+url_encode(str[1:]);
# print(str)
# print signature(str,"testsecret&")

# print getSign(parameters,"testsecret");