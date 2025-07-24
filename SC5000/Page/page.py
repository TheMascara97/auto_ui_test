'''
可以将页面封装在这里，然后在用例中直接调用这个文件，来组装成用例
'''
from Base_Command.base_conmand import BaseCom   # 导入基础命令类
from Element_Load.page_element import *     # 导入页面元素
from Test_Base_Env.test_data import *   # 导入所有的环境数据
import time

# 登录页面,继承基础命令类
class LoginPage(BaseCom):
    BaseCom().open(login_url)
    time.sleep(3)
    BaseCom().send_keys("By.XPATH", Password_element, password)
    time.sleep(4)
    BaseCom().click("By.XPATH", Login_button)
    time.sleep(3)
# class Basic_WIFI(BaseCom):
#     BaseCom().get_element_value("By.XPATH", two_SSID, "value")
#     BaseCom().get_text("By.XPATH", two_conntect)



