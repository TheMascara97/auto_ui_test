"""
对基础命令的二次封装，还可以封装断言，错误时元素标红等等
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
class BaseCom:
    # 实例化webdiver以及等待和窗口最大化
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 打开浏览器

    def open(self, url):
        self.driver.get(url)
    # 发送文本

    def send_keys(self, method, element, context):
        self.driver.find_element(eval(method), element).send_keys(context)
    # 点击

    def click(self, method, element):
        self.driver.find_element(eval(method), element).click()
    # 获取元素的文本

    def get_text(self, method, element):
        text = self.driver.find_element(eval(method), element).text
        print(text)
    # 获取页面的title

    def get_title(self):
        title = self.driver.title
        return title
    # 获取页面的url

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
    # 获取属性的值

    def get_element_value(self, method, element, attribute):
        value = self.driver.find_element(eval(method), element).get_attribute(attribute)
        print(value)
    def ActionChains(self, method, element):
        ActionChains(self.driver).move_to_element(self.driver.find_element(eval(method), element)).perform()

    # 切换窗口

    def switch_window(self):
        windows = self.driver.window_handles
        current_window = self.driver.current_window_handle
        index = windows.index(current_window)
        self.driver.switch_to.window(windows[index+1])
    # def Enter(self, method, element):
    #     search_box = self.driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)




if __name__ == "__main__":
    BaseCom().open('https://192.168.81.1')
