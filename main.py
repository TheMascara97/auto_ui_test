"""--html=report.html需要安装pytest-html"""

import pytest


if __name__ == '__main__':
    pytest.main(["-vs", "./TestCase/TestCase.py", "--html=./report/report1.html"])