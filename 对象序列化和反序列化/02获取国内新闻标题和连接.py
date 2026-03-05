import requests
resp=requests.get('https://apis.tianapi.com/guonei/index?key=a7b626742817403d6f6dfcbf649c7b84')
if resp.status_code==200:
    data_model = resp.json()
    new_list = data_model['result']['newslist'] # 获取新闻列表
    for news in new_list:
        print(f"标题: {news['title']}")
        print(f"链接: {news['url']}")
        print("---")
else:
    print(f"请求失败，状态码：{resp.status_code}")  