import os,time
from time import sleep
from original.listpage_price import detil_href_list,list_price_list,browser
from original.global_var_original import detailScreenshot

sleep(5)

detil_price_list=[]
for i in detil_href_list:
    detil_page=browser.get(i)
    sleep(3)
    #price = browser.find_element_by_xpath(r'/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2]').text
    price = browser.find_element_by_xpath(r'//div[@class="price-num"]/span[2]').text
    detil_price_list.append(price)
    detailScreenshot()

print('price in listpage:',list_price_list)
print('price in detialpage:',detil_price_list)
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2]已返
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/li[5]/div/div[1]/div/div[1]/span[2]
#//*[@id="product-container"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[5]/div/div[1]/div/div[1]/span[2] 已减
