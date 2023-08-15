import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.util import get_webdriver
from selenium.webdriver.common.by import By
from pickle import load, dump


class DamaiTicket:

    def __init__(self, ticket_web_url, username, password):
        self.driver = get_webdriver()
        self.username = username
        self.password = password
        # CDP的方式隐藏浏览器特征
        #       self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #           "source": """
        #   Object.defineProperty(navigator, 'webdriver', {
        #     get: () => undefined
        #   })
        # """
        #       })

        self.ticket_web_url = ticket_web_url

    def damai_login(self):
        # 隐式等待2s
        self.driver.implicitly_wait(2)

        # 启动浏览器并打开配置文件的网站
        self.driver.get(self.ticket_web_url)

        # 点击登录按钮
        login_btn = self.driver.find_element(By.CLASS_NAME, "span-user")
        login_btn.click()

        # 切换到对应的iframe组件
        login_iframe = self.driver.switch_to.frame("alibaba-login-box")

        # 输入账号密码登录
        username_input = self.driver.find_element(By.ID, "fm-login-id").send_keys(self.username)
        pwd_input = self.driver.find_element(By.ID, "fm-login-password").send_keys(self.password)

        # 点击登录按钮
        login_btn = self.driver.find_element(By.CLASS_NAME, "password-login")
        login_btn.click()


    def damai_quit(self):
        # 抢票完成 退出浏览器
        self.driver.quit()
