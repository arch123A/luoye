import time

from  selenium import webdriver


web=webdriver.Chrome(r"C:\Users\Surface\AppData\Local\Google\Chrome\Application\chromedriver")
web.set_window_size(1920,1080)
web.get("https://www.baidu.com/")
web.find_element_by_id("kw").send_keys("中国")
web.find_element_by_id("su").click()
# print(web.page_source)
s_cookies=web.get_cookies()
dict_cookies={i['name']:i['value'] for i in s_cookies}
print(dict_cookies)
print(web.current_url)
time.sleep(3)
web.close()
