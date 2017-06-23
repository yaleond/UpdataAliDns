# coding=UTF-8
#!/usr/bin/env python
__author__ = 'witon_an'

import sign,urllib2,json


#获取所有A记录解析记录：
#返回dict
def DescribeDomainRecords(DNSURL,Access_Key_Secret,para):
    Timestamp = sign.getTimeUTC();
    p = {};
    p["Action"] = "DescribeDomainRecords";
    p["TypeKeyWord"] = "A";

    para["Timestamp"] = Timestamp;
    para["SignatureNonce"] = Timestamp;

    parameters = dict(para,**p);
    url = getURL(DNSURL,Access_Key_Secret,parameters);
    opener = urllib2.urlopen(url);
    str = opener.read();
    return json.loads(str);

#更新记录中的value值
def UpdateDomainRecord(DNSURL,Access_Key_Secret,para,rec,ip):
    Timestamp = sign.getTimeUTC();
    para["Timestamp"] = Timestamp;
    para["SignatureNonce"] = Timestamp;

    rec["Value"] = ip;
    rec["Action"] = "UpdateDomainRecord";

    parameters = dict(para,**rec);
    # print parameters;
    # return
    url = getURL(DNSURL,Access_Key_Secret,parameters);
    opener = urllib2.urlopen(url);
    str = opener.read();
    return json.loads(str);


def getURL(DNSURL,Access_Key_Secret,para):
    return DNSURL + "?Signature="+sign.getSign(para,Access_Key_Secret)+"&"+sign.getURLWithPara(para);