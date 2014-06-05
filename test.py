import urllib2
import re

if __name__ == "__main__":
#     print "start"
#     text = urllib2.urlopen("http://aqicn.org/city/shanghai/").read()
#     print type(text)
#     text = text.encode("UTF-8")
#     print text
#    text = r"<td id='cur_pm25' class='tdcur' align=center><div class='saqi item' style='text-shadow: 1px 1px 0 #ffffff;color:#000000;background-color:#ffde33;'>87<sssdfd"
    pattern = re.compile("cur_pm25[\w=' ]+><[\w=';:\- ]+")
#    m = re.search(pattern,text)
#    print m.string