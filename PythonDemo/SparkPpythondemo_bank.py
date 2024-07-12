# coding: utf-8
import PythonDemo.SparkApi

Spark_url = 'wss://spark-api.xf-yun.com/v3.1/chat'
appid = ''
api_secret = ''
api_key = ''
domain = ''

# 初始上下文内容，当前可传system、user、assistant 等角色
text = [
    # {"role": "system", "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。"} , # 设置对话背景或者模型角色
    # {"role": "user", "content": "你是谁"},  # 用户的历史问题
    # {"role": "assistant", "content": "....."} , # AI的历史回答结果
    # # ....... 省略的历史对话
    # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
]


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


def UseSpark(text):
    # Input = input("\n" + "我:")
    question = checklen(getText("user", text))
    PythonDemo.SparkApi.answer = ""
    # print("星火:", end="")
    PythonDemo.SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    # print(SparkApi.answer)
    rusult = getText("assistant", PythonDemo.SparkApi.answer)
    return rusult


if __name__ == '__main__':
    while True:
        Input = input("\n" + "我:")
        question = checklen(getText("user", Input))
        PythonDemo.SparkApi.answer = ""
        print("星火:", end="")
        PythonDemo.SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        # print(SparkApi.answer)
        getText("assistant", PythonDemo.SparkApi.answer)
