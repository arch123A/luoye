from selenium import webdriver
import time

web = webdriver.Chrome ( r"C:\Users\Surface\AppData\Local\Google\Chrome\Application\chromedriver" )
web.get ( "https://email.163.com/" )

# web.find_element_by_class_name("account-tab-account").click()
# web.find_element_by_css_selector(".account-tab-account").click()
web.find_element_by_id("auto-id-1556109629779").send_keys("mw821009")
web.find_element_by_name("password").send_keys("mwbbt123")
web.find_element_by_id("dologin").click()
print(web.get_cookies())
time.sleep(5)
web.close()