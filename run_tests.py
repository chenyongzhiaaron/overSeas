import unittest
import logging
from HTMLTestRunner import HTMLTestRunner
from Conf import ConfTime, ConfPath

if __name__ == "__main__":
    """
    定义测试用例的目录为当前目录
    获取当前日期和时间
    调用 HTMLTestRunner，运行测试用例
    """
    # 指定测试用例为当前文件夹下的 interface 目录
    test_dir = ConfPath.TestDataPath
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    # test_data.init_data()  # 初始化接口测试数据
    now = ConfTime.CurrentTime
    html_report = ConfPath.ReportPath + now + '_TestReport.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口测试报告',
                            description='Implementation Example with: 测试环境接口测试报告')
    logging.info("------------自动化测试 action ---------------")
    print(logging.info("------------自动化测试 action ---------------"))
    runner.run(discover)
    print(logging.info("------------自动化测试 end ---------------"))
    fp.close()
    # 发送报告
    # send_mail(html_report)
