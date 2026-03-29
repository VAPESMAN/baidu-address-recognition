# -*- coding: utf-8 -*-
"""
百度NLP地址识别 - 循环版（可以一直输入）
"""

from aip import AipNlp

# 你的百度AI凭证
APP_ID = '122588652'
API_KEY = 'hNTTv9eY11Yys1IVq7EdlaFL'
SECRET_KEY = 'FwE4jMr7Kuwj7HdtxJnWXAMvCOB26GgB'

# 创建客户端
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

while True:
    # 输入地址
    text = input("\n请输入地址（输入q退出）：")
    
    if text == 'q':
        break
    
    # 识别地址
    result = client.address(text)
    
    # 输出结果
    print(f"省：{result.get('province', '')}")
    print(f"市：{result.get('city', '')}")
    print(f"区：{result.get('county', '')}")
    print(f"街道：{result.get('town', '')}")
    print(f"详细：{result.get('detail', '')}")
