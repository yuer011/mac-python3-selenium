import re
from time import sleep

from optimize.global_var import browser  # ,listScreenshot

#browser = webdriver.Chrome()    ##open ihotel.elong.com


a=browser.page_source
sleep(1)
hotelid = set(re.findall('\<a href="\/(.*?)\/\?source_id=',str(a)))    #<a href="/540636/?source_id=760844390633634504_1545044749_0_1_1_163_9_0b0
print('hotelid set is:',hotelid) #set
sleep(3)

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
        #print('暂无报价:', price_null, i)
        list_price_list.append('暂无报价')
        price_null.screenshot('/Users/user/Desktop/ui自动化相关/接口自动化/photos')
    elif isElementExist(xpath2):
        #price_saleout = browser.find_element_by_xpath(xpath2).text # 已售完
        #print('已售完', price_saleout, i)
        list_price_list.append('已售完')
    else:
        print('all is not exit')
print('price in listpage is:',list_price_list)

#listScreenshot()








'''

for i in hotelid:

    xpath='//*[@id="'+i+'"]/div/div[2]/div[1]/div[1]/p[1]/a/span[1]/span[2]'  #has price
    xpath_null='//*[@id="'+i+'"]/div/div[2]/div[1]/p'

    xpath_list.append(xpath)
    detil_href='http://ihotel.elong.com/'+i+'/'
    detil_href_list.append(detil_href)

    try:
        print('*************try********')
        price_has=browser.find_element_by_xpath(xpath).text
        print('price_has is ¥:', price_has,i)

    except:
        print('***********except****************')
        xpath1='//*[@id="'+i+'"]/div/div[2]/div[1]/p' #暂无报价
        price_null=browser.find_element_by_xpath(xpath1).text
        print('price_null is:',price_null,i)
    else:
        print('*************else********')
        xpath2 = '//*[@id="' + i + '"]/div/div[2]/div[1]/div[2]'  # 已售完
        price_saleout = browser.find_element_by_xpath(xpath2).text
        print('price_saleout is:', price_saleout,i)

    #price=browser.find_element_by_xpath(xpath).text

    ##else:
      #  print('fales')
    #list_price_list.append(price)
#print(list_price_list)

'''
#//*[@id="117078"]/div/div[2]/div[1]/p
#//*[@id="304787"]/div/div[2]/div[1]/p  暂无报价
#//*[@id="117524"]/div/div[2]/div[1]/div[2] 已售完icon
#//*[@id="119142"]/div/div[2]/div[1]/div[1]/a已售完

'''
语法解释：

try:
     表达式 1（如果表达式，可以成功执行，则执行，跳到 finally 语句）

except ExpectErrorType, Argument:   （表达式1 没有做成功，且正好是 ExpectErrorType 的错误情况，则执行）
     表达式2 （如何处理这种异常情况）
else:  （try succ && 上面 except 语句任一满足 ）之外的情况处理方法
  .....
finally:
    .... 无论什么情况都会的处理
'''