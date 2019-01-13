from time import sleep
import re
import re
from time import sleep

from original.global_var_original import browser,listScreenshot



#regionid=browser.find_element_by_class_name('text').clear()    # 这样会被识别成爬虫
#browser.find_element_by_class_name('text').send_keys('明洞')
#text=browser.find_element_by_xpath('//*[@id="hotData0"]/a[4]').click()

#**********************选择入离时间****************

indate_click=browser.find_element_by_id('inDate').click()
indate1=browser.find_element_by_xpath('//*[@id="_calendar_"]/div/div[2]/table[2]/tbody/tr[5]/td[3]').click()
sleep(3)
#outdate_click=browser.find_element_by_id('_out_calendar_').click()
#outdate1=browser.find_element_by_xpath('//*[@id="_out_calendar_"]/div/div[2]/table[1]/tbody/tr[5]/td[6]').click()
#sleep(3)


search=browser.find_element_by_class_name('com_iconsearch')   #cleck search and goto list page
search.click()
#browser.find_element_by_name('搜索').click()
print('press search')
sleep(5)
print('press search is ok')
a=browser.page_source
sleep(5)

#print(type(a))  #<class 'str'>
hotelid = set(re.findall('\<a href="\/(.*?)\/\?source_id=',str(a)))    #<a href="/540636/?source_id=760844390633634504_1545044749_0_1_1_163_9_0b0
print('hotelid set is:',hotelid) #set
sleep(1)

#hotelid1 = set(re.findall('\<a href="\/(\d+?)\/\?',str(a)))
#print('hotelid1 set is:',hotelid1) #set

#print('************css************')
#text=browser.find_element_by_class_name('h_pri_num').text
#print('classname price is:',text)
#print('************xpath************')
#price=browser.find_element_by_xpath(r'//*/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]').text
#print('xpath price is:',price)
#urls=driver.find_elements_by_xpath("//a") forurlinurls: print(url.get_attribute("href"))

xpath_list=[]
detil_href_list=[]
list_price_list=[]
for i in hotelid:
    xpath='//*[@id="'+i+'"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]'
    xpath_list.append(xpath)
    detil_href='http://ihotel.elong.com/'+i+'/'
    detil_href_list.append(detil_href)
    price=browser.find_element_by_xpath(xpath).text
    list_price_list.append(price)


#listScreenshot()
    #print(xpath,detil_href,price)

#//*[@id="550127"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]




#//*[@id="550127"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]
#//*[@id="540636"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]
#//*[@id="283668"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]
#http://www.cnblogs.com/hanmk/p/8997786.html