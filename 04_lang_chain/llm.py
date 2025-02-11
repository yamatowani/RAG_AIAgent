# -*- coding: utf-8 -*-
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat_model = ChatOpenAI(model_name="gpt-4o", temperature=0)

messages = [HumanMessage(content="自己紹介をしてください utf-8で返して")]
response = chat_model(messages)
print(response.content)
