from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

wait = WebDriverWait(driver, 3)
searchInput = driver.find_element(By.NAME, "q")
time.sleep(10)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER) # arama bölümüne entere basıldığında arama yapar
result = driver.find_elements_by_css_selector(".repo-list-item") # eğer birden fazla eleman ile işimiz varsa element değil elements kullanılır
driver.close()


# seleniumda güncelleme olduğu için kodlar çalışmadı

