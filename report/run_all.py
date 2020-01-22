#coding:utf-8
import unittest
import time
from common import HTMLTestRunner

def all_case():
#执行测试用例的目录
    case_dir = r"D:\program\Study\SeleniumStudy\test_case"
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    #discover方法筛选出来的用例,循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTest(test_case)
            print(testunit)
    return testunit

alltestnames = all_case()
print(alltestnames)


if __name__ == "__main__":

    # runner=unittest.TextTestRunner()

    now = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time())) #输出当前时间

    fp=open("result"+now+".html","wb")

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'selenium测试用例',description=u'运行环境：Windows，Chrome ')

    runner.run(alltestnames)

    fp.close()



# testReport = '/Users/soumoemoe/Documents/mararunAutoTest/testReport'
# newReport = sendEmail.newReport(testReport)
# sendEmail.sendMail(newReport)