from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chorme()
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        userInput = self.browser.find.element_by_xpath("//*[@id=loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find.element_by_xpath("//*[@id='loginForm']/div/div[1]/div/div")

        userInput.send_keys(self.user)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

instgrm =Instagram(username, password)
instgrm.signIn()