import unittest
import requests
import json
from Common import function
from parameterized import parameterized


class LoginByPassWord(unittest.TestCase):
    """密码登陆接口"""

    def setUp(self):
        self.url = function.DefTools.url(self, '/usercenter/sys/loginByPass')

    @parameterized.expand([
        ('手机号密码正确，登陆成功', "2.6.0", "15", "867910035562539", "1", "1003", "sinaif", "ef70fb3178dccde19df9295a68aca0a3",
         "qsj",),
        ('手机号密码正确，登陆成功', "2.6.0", "15", "867910035562539", "1", "1003", "sinaif", "ef70fb3178dccde19df9295a68aca0a3",
         "qsj",),
    ])
    @unittest.skip("jhjhkgjk")
    def test_login_by_password(self, name, ver, verno, deviceId, deviceType, productId, channelId, deviceToken,
                               mjbname):
        """ 测试密码登陆接口"""
        username = int()
        password = "8ff15b24341602becdf011679ec383c1"
        pa = {"ver": ver, "password": password,
              "verno": verno, "deviceId": deviceId, "deviceType": deviceType, "productId": productId,
              "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname, "username": username}
        self.params = function.DefTools().payload(**pa)
        self.result = requests.post(url=self.url, data=self.params).json()
        self.assertEqual(self.result["msg"], "ok")
        self.assertEqual(self.result["code"], 200)
        self.assertEqual(self.result['data']['username'], str(username))
        self.assertEqual(self.result['data']['mobile'], str(username))


    def tearDown(self):
        print("请求地址为{}".format(self.url))
        print("请求参数为{}".format(json.dumps(self.params, indent=2, sort_keys=False, ensure_ascii=False)))
        print("请求结果为：{}".format(json.dumps(self.result, indent=2, sort_keys=False, ensure_ascii=False)))


if __name__ == '__main__':
    unittest.main()
