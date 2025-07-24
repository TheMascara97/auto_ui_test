"""
conftest文件是pytest每次执行前都会执行的文件,所以可以将一下需要提前执行的东西放在这儿,注意搭配pytest的装饰器
"""

import pytest
import logging
from Page.page import LoginPage


# 每次test用例执行前先执行登录
@pytest.fixture(scope="session")
def db_connection():
    LoginPage()


# 打印日志
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()
    if report.when == "call":
        logging.info(f"用例ID:{report.nodeid}")
        logging.info(f"测试结果：{report.outcome}")
        logging.info(f"故障表示：{report.longrepr}")
        logging.info(f"异常：{call.excinfo}")
        logging.info(f"用例耗时：{report.duration}")
        logging.info("------------------------------")




