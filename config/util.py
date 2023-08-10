# 获取用户抢票配置文件
import json
from selenium import webdriver


def get_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config_list = json.load(f)

    except BlockingIOError:
        print("###找不到配置文件，请检查###")

    else:
        return config_list


# 配置谷歌浏览器驱动，获取webdriver
def get_webdriver():
    # 设置不自动关闭浏览器
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # 窗口最大化
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    return driver
