#!/usr/bin/env python
# coding: utf-8

# In[1]:
# -*- coding: utf-8 -*-
import json
import os
import dashscope
from dashscope.api_entities.dashscope_response import Role

# 从环境变量中，获取 DASHSCOPE_API_KEY
api_key = 'sk-6944a1b07b224ef28aeb06b0eba1aa1b'
dashscope.api_key = api_key

# 封装模型响应函数
def get_response(messages):
    response = dashscope.Generation.call(
        model='deepseek-v3',
        messages=messages,
        result_format='message'  # 将输出设置为message形式
    )
    return response
    
review = '这款音效不咋地。'
messages=[
    {"role": "system", "content": "你是一名舆情分析师，帮我判断产品口碑的正负向，回复请用一个词语：好 或者 烂透了"},
    {"role": "user", "content": review}
  ]

messages.append({"role": "assistant", "content": "烂透了"})
messages.append({"role": "user", "content": "这个音效怎么烂透了？"})

response = get_response(messages)
print(response.output.choices[0].message.content)
print(messages)

