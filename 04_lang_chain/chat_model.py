from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model_name="gpt-4o", temperature=0)

messages = [
  SystemMessage("You are a helpful AI Assistant"),
  HumanMessage("こんにちは"),
  AIMessage("こんにちは!何かお手伝いできることはありますか？"),
  HumanMessage(content="私の国籍はわかりますか？"),
]

ai_message = model.invoke(messages)

print(ai_message.content)
