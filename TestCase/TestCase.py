"""
这里可以用来写用例,直接将page封装好的各个页面拿来组装成用例
"""

from Element_Load import page_element
from Page.page import *
import pytest, logging
import time
from Base_Command import base_conmand

button = BaseCom()  # 实例化基础命令类





def test_wifi_status(db_connection):
    
    # text1=BaseCom().get_text("By.XPATH", two_status)
    # text2=BaseCom().get_text("By.XPATH", five_status)
    # assert text1=="开启" and text2=="开启"
    # BaseCom().click("By.XPATH",basic_device)
    BaseCom().click("By.XPATH",Advanced_settings)
    time.sleep(3)
    BaseCom().click("By.XPATH",LAN)
    time.sleep(3)
    BaseCom().click("By.XPATH",DHCP_server)
    
   
    
    # BaseCom().get_element_value("By.XPATH",current_link2,"value")
    
    
    # time.sleep(3)
    # BaseCom().click("By.XPATH",basic_device)
    # time.sleep(3)


    
   




