import os,time
from time import sleep
from original.listpage_price import detil_href_list,list_price_list,browser
from original.global_var_original import detailScreenshot,isElementExist

sleep(5)

detil_price_list=[]

# 新开一个窗口，通过执行js来新开一个窗口
#js='window.open("https://www.sogou.com");'
#browser.execute_script(js)


'''
for i in detil_href_list:
    detil_page=browser.get(i)
    sleep(3)
    #price = browser.find_element_by_xpath(r'/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2]').text
    price = browser.find_element_by_xpath(r'//div[@class="price-num"]/span[2]').text
    detil_price_list.append(price)
    detailScreenshot()

print('price in listpage:',list_price_list)
print('price in detialpage:',detil_price_list)
'''
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2]已返
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/li[5]/div/div[1]/div/div[1]/span[2]
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2] 已减


xpath_hasPrice = '//div[@class="price-num"]/span[2]'
xpath_saleout = '//*[@id="product-container"]/div/div[2]/div[2]/div/span/span[1]'

for i in detil_href_list:
    #js = 'window.open(i);'
    #browser.execute_script(js)
    detil_page=browser.get(i)
    time.sleep(3)




    if isElementExist(xpath_hasPrice):

        price = browser.find_element_by_xpath(xpath_hasPrice).text
        detil_price_list.append(price)
    elif isElementExist(xpath_saleout):
        detil_price_list.append('已售完')
    else:
        detil_price_list.append('获取失败')
    #price = browser.find_element_by_xpath(r'/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2]').text
    #price = browser.find_element_by_xpath(r'//div[@class="price-num"]/span[2]').text
    #detil_price_list.append(price)
    #detailScreenshot()
print('price in detialpage:',detil_price_list)