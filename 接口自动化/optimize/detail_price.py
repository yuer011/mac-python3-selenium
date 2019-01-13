import time

from optimize.global_var import isElementExist, browser
from optimize.list_price import detil_href_list

xpath_hasPrice = '//div[@class="price-num"]/span[2]'
xpath_saleout = '//*[@id="product-container"]/div/div[2]/div[2]/div/span/span[1]'
detil_price_list=[]


for i in detil_href_list:
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
print('price in detialpage:',detil_price_list)


#//*[@id="product-container"]/div/div[2]/div[2]/div/span/span[1]   已售完