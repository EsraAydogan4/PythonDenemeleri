from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("http://www.apple.com")
baslik = driver.current_url

if "apple.com" in baslik:
    print("Doğru Aplle sayfasındasınız"+baslik)

print("şu anki başlık: "+baslik)
driver.get("http://www.etsy.com")
baslik = driver.current_url
print("şu anki başlık: "+baslik)
