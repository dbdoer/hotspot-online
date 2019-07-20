# -*- coding:utf-8 -*-
import os
import time
import requests
from lxml import etree

str1 ='''{"name":"'''
str2 ='''","url": "'''
str3 ='''"},'''
try:
    os.mkdir("json")
except:
    print("json文件夹已经存在！")
#百度今日热点事件排行榜
baidu_today = "http://top.baidu.com/buzz?b=341"
#实时热点排行榜
baidu_ssrd = "http://top.baidu.com/buzz?b=1"
def parse_baidu(baidu_url,fname):
    fname = os.getcwd()+"\\json\\" +fname
    r = requests.get(baidu_url)
    r.encoding='gb2312'
    soup = etree.HTML(r.text)
    str_list = ""
    for soup_a in soup.xpath("//a[@class='list-title']"):
        hot_name = soup_a.text
        hot_url = soup_a.get('href')
        str_list = str_list + str1 + hot_name + str2+ hot_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list) 

#知乎全站热榜
def zhihu_rb():
    fname = os.getcwd()+"\\json\\" +"zhihu.json"
    zhihu_all = "https://www.zhihu.com/hot"
    headers = {'user-agent':'Baiduspider',
               'cookie':'_zap=c9245bd9-4c33-4336-8ba8-5b3dd669f112; _xsrf=25zbdplpf8g1eOTx8liThpJvjXIKNFpU; d_c0="AHCjLZP2vA-PTm5R4BJliqFfV0GHoca7-pc=|1563159142"; q_c1=03225c2e9e0c496fbd456e6b19b22d2c|1563358352000|1563358352000; __utmv=51854390.100-1|2=registration_date=20161012=1^3=entry_date=20161012=1; tst=h; __utma=51854390.1006290711.1563358355.1563358355.1563540380.2; __utmz=51854390.1563540380.2.2.utmcsr=360doc.com|utmccn=(referral)|utmcmd=referral|utmcct=/content/18/0119/13/25592655_723341899.shtml; tgw_l7_route=060f637cd101836814f6c53316f73463; tshl=; capsion_ticket="2|1:0|10:1563586609|14:capsion_ticket|44:ODIwNzM4N2I0YWJjNDczMzgyNjllNmUwZjZlZGJjMjc=|54fa40fb14fc3e8fdf90a1e36c33278a6b2b872de7d9c914ea71eab9942d14b6"; z_c0="2|1:0|10:1563586611|4:z_c0|92:Mi4xQXBPUEF3QUFBQUFBY0tNdGtfYThEeVlBQUFCZ0FsVk5NNzRmWGdEaDl6NnJndHB2M3RCSlJIb3o4LTJlc0lKU05B|4c3cb58a8ea6615d1d6db372165a0199daed52f908ec02cd7665a41abe166a2b"'          
    }
    r = requests.get(zhihu_all,headers=headers)
    r.encoding='utf-8'
    soup = etree.HTML(r.text)
    str_list=""
    for soup_a in soup.xpath("//div[@class='HotItem-content']/a"):
        zhihu_title = soup_a.get('title')
        zhihu_url = soup_a.get('href')
        str_list = str_list + str1 + zhihu_title + str2+ zhihu_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list) 

#微博热点排行榜
def parse_weibo():
    fname = os.getcwd()+"\\json\\" +"weibo.json"
    weibo_ssrd = "https://s.weibo.com/top/summary?cate=realtimehot"
    weibo = "https://s.weibo.com"
    r = requests.get(weibo_ssrd)
    r.encoding='utf-8'
    soup = etree.HTML(r.text)
    str_list=""
    for soup_a in soup.xpath("//td[@class='td-02']/a"):
        wb_title = soup_a.text
        wb_url = weibo + soup_a.get('href')
        #过滤微博的广告，做个判断
        if "javascript:void(0)" in wb_url:
            str_list = str_list
        else:
            str_list = str_list + str1 + wb_title + str2+ wb_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)
#贴吧热度榜单
def parse_tieba():
    fname = os.getcwd()+"\\json\\" +"tieba.json"
    tb_url = "http://tieba.baidu.com/hottopic/browse/topicList?res_type=1"
    r = requests.get(tb_url)
    soup = etree.HTML(r.text)
    str_list=""
    for soup_a in soup.xpath("//a[@class='topic-text']"):
        tieba_name = soup_a.text
        tieba_url = soup_a.get('href')
        str_list = str_list + str1 + tieba_name + str2+ tieba_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#V2EX热度榜单
def parse_vsite():
    vsite_hoturl = "https://www.v2ex.com/?tab=hot"
    vsite ="https://www.v2ex.com"
    fname = os.getcwd()+"\\json\\" +"vsite.json"
    r = requests.get(vsite_hoturl)
    soup = etree.HTML(r.text)
    str_list=""
    for soup_a in soup.xpath("//span[@class='item_title']/a"):
        vsite_name = soup_a.text
        vsite_url = vsite+soup_a.get('href')
        str_list = str_list + str1 + vsite_name + str2+ vsite_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)
    


if __name__ == "__main__":
    while True:
        try:
            parse_vsite()
            parse_tieba()
            parse_weibo()
            parse_baidu(baidu_ssrd,"baidurd.json")
            parse_baidu(baidu_today,"baidusj.json")
            zhihu_rb()
        except:
            print("采集出现一个错误，请及时更新规则！")
        time.sleep(600) #每隔600秒也即十分钟更新一次
