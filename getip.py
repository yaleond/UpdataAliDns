import re,urllib2
class GetPublicIp:
    IP_ERROR = "110120119";
    def getip(self):
        try:
            myip = self.visit("http://ddns.nat123.com")
        except:
            try:
                myip = self.visit("http://1212.ip138.com/ic.asp")
            except:
                try:
                    myip = self.visit("http://ip.chinaz.com/getip.aspx")
                except:
                    try:
                        myip = self.visit("http://www.ip.cn/")
                    except:
                        myip = self.IP_ERROR;
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read();
        return re.search("\d+\.\d+\.\d+\.\d+",str).group(0);

#getmyip = GetPublicIp()
#print getmyip.getip()
