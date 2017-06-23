# coding=UTF-8
#!/usr/bin/env python


from getip import GetPublicIp
import time,method,os

DNSURL = "http://alidns.aliyuncs.com"
#https://develop.aliyun.com/api?spm=5176.doc29821.2.6.xsUCfs  从此页面进入点击创建secretID\KEY
Access_Key_ID = "Access_Key_IDAccess_Key_IDAccess_Key_ID"
Access_Key_Secret = "Access_Key_SecretAccess_Key_Secret"
Version = "2015-01-09"
DomainName = "xxxxx.com"
SignatureMethod = "HMAC-SHA1"
SignatureVersion = "1.0"
Format = "JSON"

#公式参数：
parameters = {}
parameters["Action"] = ""
parameters["DomainName"] = DomainName
parameters["Version"] = Version
parameters["AccessKeyId"] = Access_Key_ID
parameters["Timestamp"] = ""
parameters["SignatureNonce"] = ""
parameters["SignatureMethod"] = SignatureMethod
parameters["SignatureVersion"] = SignatureVersion
parameters["Format"] = Format

IPFILEPATH = os.path.expanduser('~') + "/ip"

while 1:
    try:
        ipFileR = open(IPFILEPATH, 'r')
        localIP = ipFileR.readline()
        ipFileR.close()
    except:
        localIP = '1'


    #获取外网地址：
    getmyip = GetPublicIp()
    myip =  getmyip.getip()

    #如果文本记录中的IP跟当前IP不同，就得更新文件，更新DNS
    if cmp(GetPublicIp.IP_ERROR,myip) !=0 and cmp(localIP,myip) != 0:
        try:
            #print 1
            result =  method.DescribeDomainRecords(DNSURL,Access_Key_Secret,parameters)
            # print 2
            print method.UpdateDomainRecord(DNSURL,Access_Key_Secret,parameters,result['DomainRecords']['Record'][0],myip)
            #要等待一秒后再次请求，要不然90%出错
            time.sleep(1)
	    # print 3
            print method.UpdateDomainRecord(DNSURL,Access_Key_Secret,parameters,result['DomainRecords']['Record'][1],myip)
            #print 4
            ipFileW = open(IPFILEPATH, 'w')
            ipFileW.write(myip)
            ipFileW.close()
        except Exception as e:
            print(e)

    time.sleep(60*10)



#方法参数：
# parameters["TypeKeyWord"] = "A"
#
# print(sign.getSign(parameters,Access_Key_Secret))
# print(sign.getURLWithPara(parameters))
# URL = DNSURL + "?Signature="+sign.getSign(parameters,Access_Key_Secret)+"&"+sign.getURLWithPara(parameters)
#
# opener = urllib2.urlopen(URL)
# str = opener.read()
# print(str)
# jsonR = json.loads(str)
# print jsonR['DomainRecords']['Record'][0]
# print jsonR['DomainRecords']['Record'][1]
# print(type(json.loads(str)))
# print(type(json.dumps(str)))






















