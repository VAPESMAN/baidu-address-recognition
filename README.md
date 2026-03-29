# 百度NLP地址识别工具

简单易用的地址识别工具，从文本中提取省市区街道等地址信息。

## 安装依赖

```bash
pip install requests chardet baidu-aip
```

## 使用方法

### 简单版（识别一次）
```bash
python address_simple.py
```

### 循环版（一直输入）
```bash
python address_loop.py
```

## 示例

输入：
```
北京市朝阳区三里屯SOHO
```

输出：
```
省：北京市
市：北京市
区：朝阳区
街道：三里屯街道
详细：三里屯SOHO
```

## 配置

在文件开头修改你的百度AI凭证：

```python
APP_ID = '你的App ID'
API_KEY = '你的Api Key'
SECRET_KEY = '你的Secret Key'
```

获取凭证：https://ai.baidu.com/
