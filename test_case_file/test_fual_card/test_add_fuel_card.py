import requests
import unittest
import json
from lib.sql import *
from lib.read_excel import *
from config.config import *

class Testaddfuel(unittest.TestCase):
    #正常添加
    def test_add(self):
        #数据准备
        case_data = get_data(data_file,'Testaddfuel', 'test_add')
        url = case_data[1]
        data = case_data[3]
        except_res = case_data[4]
        #环境检查
        if check_cardNumber("ycy900"):
            print("存在{}".format("ycy900"))
            del_cardNumber("ycy900")
            print("删除{}成功".format("ycy900"))
        logging.info("测试用例{}".format("test_add"))
        logging.info("url:{}".format(url))
        logging.info("data:{}".format(data))
        logging.info("except_res:{}".format(except_res))

        #发送请求
        r = requests.post(url=url, data=data)
        print(r.text)
        #响应断言、数据库断言
        self.assertEqual(str(r.text), except_res)
        self.assertIsNotNone(check_cardNumber("ycy900"))
        #数据清理
        del_cardNumber("ycy900")

    #重复添加
    def test_repeat_add(self):
        #数据准备
        case_data = get_data(data_file, 'Testaddfuel', 'test_repeat_add')
        url = case_data[1]
        data = case_data[3]
        except_res = case_data[4]
        #环境检查
        if check_cardNumber("37142000"):
            print("存在{}".format("37142000"))
        else:
            insert_cardNumber("37142000")
            print("添加{}成功".format("37142000"))
        logging.info("测试用例{}".format("test_repeat_add"))
        logging.info("url:{}".format(url))
        logging.info("data:{}".format(data))
        logging.info("except_res:{}".format(except_res))
        #发送请求
        r = requests.post(url=url,data=data)
        print(r.text)
        #响应断言、数据库断言
        self.assertEqual(r.text, except_res)
        self.assertIsNotNone(check_cardNumber("37142000"))


if __name__ == '__main__':
    unittest.main()





