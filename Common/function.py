# coding = utf-8
import base64

import requests
from natsort import natsorted
from pprint import pprint
import hashlib
import os
import logging
import json
import configparser as cparser

from pyDes import des, PAD_PKCS5


class DefTools(object):
    def url(self, patch):
        """
        :param patch: 路径
        :return: 访问url
        """
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + "/config.ini"
        cf = cparser.ConfigParser()
        cf.read(file_path)
        baseUrl = cf.get("urlTestconf", "url_test")
        url = baseUrl + patch
        return url

    def payload(self, **params):
        """
        :param params: 需要签名参数
        :return: 带签名参数
        """
        sortedList = []
        for key in params:
            try:
                sortedParms = str(key) + str(params[key])
                sortedList.append(sortedParms)
            except Exception as e:
                print("排序参数异常", e)
        sort = natsorted(sortedList)  # 列表自然排序
        argument = "a8235488a6aae009ff7e32430fee2f44"
        keysorted = argument + ("".join(sort))
        md = hashlib.md5()
        md.update(keysorted.encode(encoding='utf-8'))
        sign_old = md.hexdigest()
        sign = {"sign": sign_old}
        payload = dict(params, **sign)
        return payload

    def headers(self, token):
        """
        :param token: 用户 token
        :return: header
        """
        header = {"token": token}
        return header

    def desEncode(self, desStr):
        """
        :param desStr: 需要加密的参数
        :return: 加密后的 value
        """
        k = des('secretKEY', padmode=PAD_PKCS5)
        encodeStr = base64.b64encode(k.encrypt(json.dumps(desStr)))
        return encodeStr


class RunMain:
    """"封装各类请求：get,post,put,deleter,options,head"""

    def __init__(self, method, url, params=None, header=None, params_json=None):
        self.re = self.http_request(method, url, params, header, params_json).json()

    def http_request(self, method, url, params=None, header=None, params_json=None):
        result = None
        if method == "get":
            try:
                if header != None:
                    result = requests.get(url=url, params=params, headers=header, json=params_json)
                    logging.info("action get")
                else:
                    result = requests.get(url=url, params=params, json=params_json)
                    logging.info("action get")
            except Exception as e:
                logging.error("请求失败，→url→{}→参数→{}→header→{}".format(url, params, header))
        else:
            try:
                result = requests.post(url=url, data=params, headers=header, json=params_json)
                logging.info("action post")
            except Exception as e:
                logging.error("请求失败，→url→{}→参数→{}→header→{}".format(url, params, header))
        # return json.dumps(result.json(), indent=2, sort_keys=False, ensure_ascii=False)
        return result


if __name__ == "__main__":
    new_url = DefTools()
    url = new_url.url('/app/loan/getHomeProductListV3.do')
    print(url)
    test = RunMain("get", url).re
    pprint(test)
