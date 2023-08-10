from config.util import get_webdriver
from selenium.webdriver.common.by import By
from pickle import load, dump


class DamaiTicket:

    def __init__(self, ticket_web_url):
        self.driver = get_webdriver()
        self.ticket_web_url = ticket_web_url

    def damai_login(self):
        # 启动浏览器并打开配置文件的网站
        self.driver.get(self.ticket_web_url)

        # 点击登录按钮
        login_btn = self.driver.find_element(By.CLASS_NAME, "span-user")
        login_btn.click()

        # 点击扫码登录按钮
        scan_login_tabs = self.driver.find_elements(By.TAG_NAME, "div")
        for e in scan_login_tabs:
            print(e.name)

    def damai_quit(self):
        # 抢票完成 退出浏览器
        self.driver.quit()
