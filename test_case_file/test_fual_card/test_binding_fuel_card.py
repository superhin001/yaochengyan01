import requests
import unittest
import json
from lib.sql import *
from lib.read_excel import *

class TestBindingfuelcard(unittest.TestCase):
    #正常绑定
    def test_binding(self):
        # 数据准备
        case_data = get_data(data_file, 'TestBindingfuelcard', 'test_binding')
        url = case_data[1]
        data = case_data[3]
        except_res = case_data[4]
        #环境检查(1、如果卡号不存在，则数据库中添加；2、如果卡号已被绑定，数据库中解除绑定)
        if not check_cardNumber("ycy147"):
            print("不存在{}".format("ycy147"))
            insert_cardNumber("ycy147")
            print("添加{}成功".format("ycy147"))
        if check_cardstatus("ycy147") == 5010:
            print("卡号{}已被绑定".format("ycy147"))
            update_cardinfo("ycy147")
            print("卡号{}已解除绑定".format("ycy147"))
        logging.info("测试用例{}".format("test_binding"))
        logging.info("url:{}".format(url))
        logging.info("data:{}".format(data))
        logging.info("except_res:{}".format(except_res))
        #发送请求
        r = requests.post(url=url,data=data)
        print(r.text)
        #响应断言、数据库断言
        self.assertEqual(str(r.text), except_res)
        self.assertIsNotNone(check_cardstatus("ycy147"))
        #环境清理(解除绑定)
        update_cardinfo("ycy147")

    #重复绑定
    def test_repeat_binding(self):
        #数据准备
        case_data = get_data(data_file,'TestBindingfuelcard', 'test_repeat_binding')
        url = case_data[1]
        data = case_data[3]
        except_res = case_data[4]
        #环境检查（1、如果卡号不存在，则数据库中添加；2、如果该卡还未被绑定，则数据库中绑定）
        if not check_cardNumber('37142000'):
            print("不存在{}".format('37142000'))
            insert_cardNumber('37142000')
            print("添加{}成功".format('37142000'))
        if check_cardstatus('37142000') is None:
            print("该卡{}还未绑定".format('37142000'))
            updata_cardinfo_binding('37142000')
            print("已将该卡{}绑定成功".format('37142000'))
        logging.info("测试用例{}".format("test_repeat_binding"))
        logging.info("url:{}".format(url))
        logging.info("data:{}".format(data))
        logging.info("except_res:{}".format(except_res))
        #发送请求
        r = requests.post(url=url, data=data)
        print(r.text)
        #响应断言、数据库断言
        self.assertEqual(str(r.text), except_res)
        self.assertIsNotNone(check_cardstatus('37142000'))
        #环境清理



if __name__ == '__main__':
    unittest.main(verbosity=2)
    # A = TestBindingfuelcard()
    # A.test_binding()
    # A.test_repeat_binding()


