from time import sleep
import re
import re
from time import sleep

from original.global_var_original import browser,listScreenshot,isElementExist


#**********************选择入离时间****************

indate_click=browser.find_element_by_id('inDate').click()

sleep(5)
indate1=browser.find_element_by_xpath('//*[@id="_calendar_"]/div/div[2]/table[2]/tbody/tr[5]/td[3]').click()
sleep(5)

search=browser.find_element_by_class_name('com_iconsearch')   #cleck search and goto list page
search.click()
print('press search')
sleep(5)
print('press search is ok')
a=browser.page_source
sleep(5)

hotelid = set(re.findall('\<a href="\/(.*?)\/\?source_id=',str(a)))    #<a href="/540636/?source_id=760844390633634504_1545044749_0_1_1_163_9_0b0
print('hotelid set is:',hotelid) #set
sleep(1)

xpath_list=[]
detil_href_list=[]
list_price_list=[]

for i in hotelid:
    xpath='//*[@id="'+i+'"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]'  #有价格
    xpath1 = '//*[@id="' + i + '"]/div/div[2]/div[1]/p'  # 暂无报价
    xpath2 = '//*[@id="' + i + '"]/div/div[2]/div[1]/div[2]'  # 已售完
    detil_href = 'http://ihotel.elong.com/' + i + '/'
    detil_href_list.append(detil_href)
    if isElementExist(xpath):
        price_has=browser.find_element_by_xpath(xpath).text
        list_price_list.append(price_has)
    elif isElementExist(xpath1):
        price_null = browser.find_element_by_xpath(xpath1)#.text # 暂无报价
        list_price_list.append('暂无报价')
    elif isElementExist(xpath2):
        list_price_list.append('已售完')
    else:
        print('all is not exit')
print('price in listpage is:',list_price_list)


