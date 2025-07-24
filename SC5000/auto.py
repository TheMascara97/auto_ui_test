from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Constants:
    HTML_LOGIN = 'http://192.168.81.1/#/login'
    
    # HTML_LOGIN = 'http://192.168.81.1/#/login'

class WebAutomation:
    LOGIN_HTML = 'http://192.168.81.1/#/login'
    CHROME_DRIVER_PATH = 'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'

    def __init__(self):
        service = ChromeService(executable_path=self.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.find_component = WebDriverWait(self.driver, 20)

    def open_login_page(self):
        """打开登录页面"""
        self.driver.get(self.LOGIN_HTML)

    def login(self, password):
        """执行登录操作"""
        # 等待密码输入框出现并输入密码
        password_field = self.find_component.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'][placeholder='密码']")))
        password_field.send_keys(password)

        # 等待登录按钮可用并点击
        login_button = self.find_component.until(EC.element_to_be_clickable((By.XPATH, "//button[./span[text()='登录 ']]")))
        login_button.click()

    def keep_browser_open(self):
        input("Press Enter to close the browser...")
        self.driver.quit()

    def input_text_5g_ssid(self, text):
        css_selector = "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/input"
        input_element = self.find_component.until(
            EC.visibility_of_element_located((By.XPATH, css_selector))
        )
        input_element.clear()  # 清除可能存在的默认文本
        input_element.send_keys(text)
        
    def click_5g_eye(self):
        css_selector = "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[3]/div/div/span/span/i"
        input_element = self.find_component.until(
            EC.visibility_of_element_located((By.XPATH, css_selector))
        )
        input_element.click()  
        
    def input_text_5g_pwd(self, text):
        self.click_5g_eye()
        css_selector = "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div/div[3]/div/div/input"
        
        input_element = self.find_component.until(
            EC.visibility_of_element_located((By.XPATH, css_selector))
        )
        input_element.clear()  # 清除可能存在的默认文本
        input_element.send_keys(text)
        value = input_element.get_attribute('value')
        print(f"The input field's current value is: {value}")
    
    def to_device_info(self):
        css_selector = "/html/body/div[1]/section/section/aside/div/div/div[1]/div/ul/div/label[4]/li"
        input_element = self.find_component.until(
            EC.visibility_of_element_located((By.XPATH, css_selector))
        )
        input_element.click() 
    
    def to_device_info_get_network_info(self):
        input_element = self.find_component.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/section/section/section/main/div[1]/form/div[2]/div[2]/div[1]/div/div[1]/div/div/input"))
        )
        value = input_element.get_attribute('value')
        print(f"The input field's current value is: {value}")

if __name__ == "__main__":
    automation = WebAutomation()
    
    try:
        automation.open_login_page()
        automation.login("admin")
        # automation.input_text_5g_ssid("123123123")
        # automation.click_5g_eye()
        # automation.input_text_5g_pwd("12345678")
        # automation.click_5g_eye()
        automation.to_device_info()
        automation.to_device_info_get_network_info()

        automation.keep_browser_open()
    except Exception as e:
        print(f"An error occurred: {e}")
        automation.driver.quit()