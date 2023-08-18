from config.util import get_webdriver
from selenium.webdriver.common.by import By
import time, os, pickle


class DamaiTicket:

    def __init__(self, ticket_web_url, username, password, ticket_item_url):
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
        self.ticket_item_url = ticket_item_url
        self.cookie_file = 'cookie.pkl'
        self.cookie_dict = {}

    def enter_ticket_page(self):
        # 先打开大麦网首页
        self.driver.get(self.ticket_web_url)

        # 如果存在cookie 则直接读取文件
        if os.path.exists(self.cookie_file):
            self.get_cookie()
        # 否则需要先登录后持久化保存 cookie
        else:
            self.safe_cookie()

        print(self.cookie_dict)
        # 给driver增加带cookie登录
        self.driver.add_cookie(self.cookie_dict)
        print(self.driver.get_cookies())
        self.driver.refresh()

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
        time.sleep(1)
        pwd_input = self.driver.find_element(By.ID, "fm-login-password").send_keys(self.password)

        # 点击登录按钮
        login_btn = self.driver.find_element(By.CLASS_NAME, "password-login")
        login_btn.click()

    def get_cookie(self):
        global cookie_dict
        print('### cookie已存在，正在从文件加载 ###')
        cookies = pickle.load(open(self.cookie_file, 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': cookie.get('domain'),  # 必须有，不然就是假登录
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False}
        self.cookie_dict = cookie_dict

    def safe_cookie(self):
        # 先登录大麦网
        global cookie_dict
        self.damai_login()
        # 访问url 获取浏览器cookie
        self.driver.refresh()
        cookies = self.driver.get_cookies()
        # 二进制保存cookie文件
        pickle.dump(cookies, open(self.cookie_file, 'wb'))

        for cookie in cookies:
            cookie_dict = {
                'domain': cookie.get('domain'),  # 必须有，不然就是假登录
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False}
        self.cookie_dict = cookie_dict
        print('### cookie保存成功 ###')

    def damai_quit(self):
        # 抢票完成 退出浏览器
        self.driver.quit()
