import datetime, time,random
from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类

headers_mine={
'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3642.0 Safari/537.36',
'Accept-Encoding: gzip, deflate',
'Accept-Language: zh-CN,zh;q=0.9',
'Cookie: H5CookieGuid=277f4555-1149-c29f-4ed2-534ba9c2ad99; _RSG=pU4KN0pDAH48FcOKEj73qB; _RDG=282b0a82e5e3952d962d7ffe648d85adef; _RGUID=444a3730-1750-47b3-bd03-1ed3946263c8; CookieGuid=6fb6d4cb-5cb3-f8ec-7c7b-af6ac06b295a; __tjcount=59; _fid=jf3o970b-01a2-4a32-bcb2-7155f5150c0f; _RF1=106.121.65.122; Esid=15c5086c-98a1-4f67-9208-0786001de561; member=15001080991; Lgid=LRpRtrsC3gsExwGXhEk%2FlpaR3waA7McUH7SGryL5%2FSHEYDBV4aVez1u%2FwV9w8wXju5dxPtglCgNmcLYSGPd1fcYHvcNwLzCbXNXEwYmotlK3kTjebacYdTTr6ADGqClE6w%2BFkLgzL9dHWVussHMgLQ%3D%3D; EbkSessionId=aef6374f5723424eab4b965d54bf497e; free_tk=e3ozw%2B8q6%2BRDPbs6SkX83jA1KOUa0jab5sd88IMJzdanSx4cPJm2Ng%2FnVtgsAXtmfzdMZhqPlb4t%0AI4%2BPn2ze61%2Fqhj%2BUv7ZfEGCC2YQbhgxd%2B2oZXav%2BlNsb578dSjXEH2XmjaDprYQQIWlhm%2B5nVCQg%0ANYW0aalq; businessLine=login; H5CookieId=277f4555-1149-c29f-4ed2-534ba9c2ad99; IH5Search=%7B%22inDate%22%3A%222018-12-14%22%2C%22outDate%22%3A%222018-12-15%22%2C%22regionId%22%3A178308%2C%22regionName%22%3A%22%5Cu9996%5Cu5c14%22%7D; SessionGuid=c27b5531-8813-4d50-b6ed-362153bf2f8d; semid=ppzqbaidu; outerFrom=ppzqbaidu; fv=pcweb; ext_param=bns%3D4%26ct%3D3; s_cc=true; s_visit=1; s_eVar44=ppzqbaidu; com.eLong.CommonService.OrderFromCookieInfo=Pkid=50793&Parentid=3150&Coefficient=0.0&Status=1&Priority=9001&Makecomefrom=0&Savecookies=0&Cookiesdays=0&Isusefparam=0&Orderfromtype=5; IHParams=%7B%22ofid%22%3A%2250793%22%7D; s_sq=elongcom%3D%2526pid%253Dwww.elong.com%2526pidt%253D1%2526oid%253Dhttp%25253A%25252F%25252Fihotel.elong.com%25252F%2526ot%253DA; iv=1234567890555155; IHotelSearch=RoomPerson=1%7C2&OutDate=2018-12-25&InDate=2018-12-24&RegionName=%E5%B7%B4%E5%8E%98%E5%B2%9B&RegionId=602651&RegionNameAlpha=Bali&; IHotelSearchData=%7B%22InDate%22%3A%222018-12-24%22%2C%22OutDate%22%3A%222018-12-25%22%2C%22RegionId%22%3A%22602651%22%2C%22RegionName%22%3A%22%E5%B7%B4%E5%8E%98%E5%B2%9B%22%7D; Hm_lvt_a22d124d90c522c78514328a02b36c85=1544075354,1544077707,1544079642,1545470057; Hm_lpvt_a22d124d90c522c78514328a02b36c85=1545470061'
}



regionid_set=[178236,100003201,6046393,180027,178308,179900,890,100003301,9514,179897,180008,602651,6049718,602,3657,1079,178276,178280]
regionid=random.choice(regionid_set)    #请求regionid

today=datetime.date.today()
add_days=random.randint(0,20)
total_days=random.randint(1,5)

indate=today+datetime.timedelta(days=add_days) #indate
outdate=indate+datetime.timedelta(days=3)      #outdate

print(indate,outdate,regionid)


browser = webdriver.Chrome()
request_url = 'http://ihotel.elong.com/region_'+str(regionid)+'/?indate='+str(indate)+'&outdate='+str(outdate)
browser.get(request_url)

time.sleep(3)


def isElementExist(element):
    flag=True
    try:
        browser.find_element_by_xpath(element)
        return flag
    except:
        flag=False
        return flag

def saveScreenShot():
    # 生成年月日时分秒时间
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    #print(picture_time)
    #print(directory_time)
    # 打印文件目录
    #print(os.getcwd())  #获取当前路径
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = os.getcwd() + '/' + directory_time + '/'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            #print("目录新建成功：%s" % File_Path)
        else:
            print("图片保存目录已存在！！！")
    except BaseException as msg:
        print("新建目录失败：%s" % msg)

    #browser.get("https://baidu.com/")
    try:
        url=browser.save_screenshot('./' + directory_time + '/' + picture_time + '.png')
        print("%s ：截图成功！！！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)

#ActionChains(browser).move_to_element(****).perform()

time.sleep(5)

#将页面滚动条移动到页面任意位置，改变等于号后的数值即可
#s="var q=document.documentElement.scrollTop=600"
#browser.execute_script(js)

def listScreenshot():
    for i in range(5):
        saveScreenShot()
        browser.execute_script("window.scrollBy(0,610)")
        time.sleep(10)

def detailScreenshot():
    browser.execute_script("window.scrollBy(0,610)")
    time.sleep(10)
    saveScreenShot()


#listScreenshot()
#time.sleep(10)

#browser.quit()

#/Users/user/Desktop/ui自动化相关/接口自动化/photos