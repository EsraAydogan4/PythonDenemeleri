from selenium import webdriver
import time


driver = webdriver.Chrome()
url = "http://github.com/EsraAydogan4"
driver.get(url) 

print(driver.title)

if "EsraAydogan4" in driver.title:
    driver.save_screenshot("github-esra")
time.sleep(2)
# driver.maximize_window() # pencereyi tam ekran yapar
# driver.save_screenshot("github.com-homepage.png") # sayfanın resmini  ve kaydeder
# print(driver.title) # sayfanın başlığını konsola yazdırır

time.sleep(2)
driver.close() # pencereyi kapatır

