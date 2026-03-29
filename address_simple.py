# -*- coding: utf-8 -*-
"""
百度NLP地址识别 - 简单版
"""

from aip import AipNlp

# 你的百度AI凭证
APP_ID = 'your appid'  
API_KEY = 'your api_key'
SECRET_KEY = 'your secret_key'

# 创建客户端
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 输入地址文本
text = input("请输入地址：")

# 调用地址识别
result = client.address(text)

# 输出结果
print("识别结果：")
print(f"  省份：{result.get('province', '')}")
print(f"  城市：{result.get('city', '')}")
print(f"  区县：{result.get('county', '')}")
print(f"  街道：{result.get('town', '')}")
print(f"  详细：{result.get('detail', '')}")
print(f"  经度：{result.get('lng', '')}")
print(f"  纬度：{result.get('lat', '')}")
