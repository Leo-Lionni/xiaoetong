import os 
import requests
import re
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import logging
import sys
reload(sys)

sys.setdefaultencoding("utf-8")

logfile = "do.log"
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)


#down m3u8
def d_m3u8:
    #url0 是如何安排的呢 ，由于cookies过期，会导致问题出现；
    #直接从浏览器下载也可以，python下载也是可以的；
    url0 ="https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/d4ca5fa75285890791072075115/drm/v.f230.m3u8?t=5ebe4a78&us=382920&sign=7f9b7cf5427ca0f14bfa143ffc4f772c"

    url1 ="https://pc-shop.xiaoe-tech.com/appcFZq02Gl5628/video_details?id=v_5d1c9ab85c6d2_3F5rUM15"
    cookies =dict(cookies = "tgw_l7_route=2d717cf374b1dfdf3a7462dcd4d4f62c; laravel_session=eyJpdiI6IlV4VEY3V2h6STUyU01FVTZqVDQ2SkE9PSIsInZhbHVlIjoiOWRnSHlTeUtKQktNak52VmhKZ3g4enhIQ2pKWWhJUzBudzBCQlZFcFd6eUVBRHNDR2hDcHVKQ283cUpMWDJjODg4ejNYT2tJVU5oa3FVNzZLQjRiNGc9PSIsIm1hYyI6IjZlZDZhNjZlMTM4MGE5YTNmNGEwYThlZmZlY2VjOTQyZTRiZjUwYTMwNDcwYmYyZDcwYzM1NmU2Nzc0YmFiOGEifQ%3D%3D")
    myheader = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.34 Safari/537.36 Edg/81.0.416.20',
 }
    resp1 =requests.get(url1,headers=myheader,verify=False,cookies=cookies)
    if(resp1.status_code != 200){
        print("network error")
        return 
    }
    #url2是请求二进制key
    # url2  ="https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/d4ca5fa75285890791072075115/drm/v.f230.m3u8?t=5ebe25b9&us=295839&sign=2b78b89e15f75a0f430ee9c7a8d567c9"
    url2 = "https://app.xiaoe-tech.com/get_video_key.php?edk=CiDkLPJ7dDl5HKu%2FSv%2B21G7JQTJMZbSy1wPoQ1SAgsLSqhCO08TAChiaoOvUBCokYjRhNjFiNTgtMmVhNy00OWYxLTgwZGMtZTE0NTIyODc5YWIy&fileId=5285890791072075115&keySource=VodBuildInKMS"

    resp1 =requests.get(url2,verify=False,cookies=cookies,headers=myheader)
    
    print("当前访问并即将保存m3u8文件",resp1.status_code)
    sava_to(resp1.content)  
    print("保存m3u8文件ok")
    
    # print("进行读取并筛选")
    # list_content = resp1.text.split('\n')
    # player_list= []
    # for i, l in enumerate(list_content):
    #     if "#EXE-X-KEY" in l:
    #         method_pos = l.find("METHOD")
    #         comma_pos = l.find(",")
    #         method = l[method_pos:comma_pos].split("=")[1]
    #         print("Decode Method:",method)
    #         uri_pos=l.find("URI")
    #         qutation_mark_pos =l.rfind('"')
    #         key_path = l[uri_pos:qutation_mark_pos].split('"')[1]
    #         key_url = key_path
    #         res 

    # print(r)

def save_to_b(content,filepath):
    #e二进制保存数据；key
    with  open(filepath,"wb") as f:
        f.write(content)
def save_to(content,filepath):
    #e二进制保存数据；key
    with  open(filepath,"w") as f:
        f.write(content)   
#返回m3u8文件内部的按行读取的列表
def read_file_as_str_list(file_path):
    #/Users/chy/Downloads/file_ts/v.f230.m3u8
    if not os.path.isfile(file_path):
        raise TypeError(file_path+"does not exist")
    # text = open(file_path).split("\n")

    all_the_text_list= open(file_path).readlines()
    return all_the_text_list
def add_in_list():
    basepath ="https://vod2.xiaoe-tech.com/9764a7a5vodtransgzp1252524126/d4ca5fa75285890791072075115/drm/"
    addlists = []
    lists=read_file_as_str_list("./v.f230.m3u8")
    for l  in lists:
        if "v.f230" in l:
            print("exists")
            url="v"+GetMiddleStr(l,"v","\n")
            addlists.append(basepath+url)

    
    return addlists
        


# def read_from():
#     with open("./m3u8_key","rb") as f:
#         f.seek(0,0)
#         while True:
#             byte =read(1)
#             if byte == '':
#                 break
#             else:
#                 hexstr = "%s" % byte.encode('hex')
#                 decnum = int(hexstr , 16)
#             print(byte ,hexstr,decnum)
#         f.close()
#         print("finish")

#down all ts(encryted)
def GetMiddleStr(content,startStr,endStr):
    patternStr = r'%s(.+?)%s'%(startStr,endStr)
    p = re.compile(patternStr,re.IGNORECASE)
    m= re.match(p,content)
    if m:
        #这里不可是（） 内建函数或者方法对象不能subscriptable
        return m.group(1)

def d_all_ts:
    url_per_list=[]
    # filepaht =
    lines = read_file_as_str_list(file_path)
    for line in lines:
        need_url = GetMiddleStr(line,"v","\n")
        needs_url = []
        if(need_url):
            needs_url.append(need_url)

    # return needs_url
    for one_url in needs_url:
        resp = requests.get(one_url,cookies=cookies,headers=myheader,verify = False)
        save_to(resp.content,"./")
        print("one OK")
    

        

    
    
# def d_one_ts:
#      for  in 
#          pass   
# def decry_all_t

# def concat_all_ts:
    



if __name__ == "__main__":
    d_m3u8()
    d_all_ts()


