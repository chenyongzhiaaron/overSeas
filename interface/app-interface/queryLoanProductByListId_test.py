import requests
import unittest
from Global_base import global_base,login,globa_phone
from parameterized import parameterized


class QueryLoanProductByListId(unittest.TestCase):
    '''轻松借模块列表接口'''
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/loan/queryLoanProductByListId.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("查询模块列表", "NPL6320190619171559100", "", "1003", "1", "true",
         "2.6.0", 1, 1, "867910035562539")
    ])
    def test_queryLoanProductByListId(self, case, id, tags, productId, clientType, queryRecProduct, versionName,
                                      queryType, dataType, deviceId):
        values = login.LoginByPassWord().login_by_password(int(globa_phone.phone()))
        userId = values[0]
        token = values[1]
        pa = {"id": id, "tags": tags, "deviceId": deviceId,
              "productId": productId, "userId": userId, "token": token, "clientType": clientType, "queryRecProduct":queryRecProduct, "versionName":versionName, "queryType":queryType, "dataType":dataType}
        params = global_base.DefTool().payload(**pa)
        token = "2782e95b1cffcc59026cab695c2e86eb1"
        header = {"token": token}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result['code'], '200')


if __name__ == '__main__':
    unittest.main()
