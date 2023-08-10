from config.util import get_config
from channel.damai_ticket import DamaiTicket

# 获取抢票配置文件
config_path = 'config/config.json'
user_config = get_config(config_path)

# 传入配置文件参数 自动化抢票
damai_ticket = DamaiTicket(user_config['ticket_web_url'])
# 打开浏览器登录
print('##### 打开浏览器 #####')
damai_ticket.damai_login()

# 关闭浏览器
print('##### 关闭浏览器 #####')
damai_ticket.damai_quit()
