from langchain_community.document_loaders import GitLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI



embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def file_filter(file_path: str) -> bool:
  return file_path.endswith(".mdx")

loader = GitLoader(
  clone_url="https://github.com/langchain-ai/langchain",
  repo_path="./langchain",
  branch="master",
  file_filter=file_filter,
)
documents = loader.load()

db = Chroma.from_documents(documents, embeddings)


prompt = ChatPromptTemplate.from_template('''\
以下の文脈だけを踏まえて質問に回答してください
文脈"""
{context}
"""

質問: {question}
''')

model = ChatOpenAI(model='gpt-4o', temperature=0)

retriever = db.as_retriever()

chain = {
  "question": RunnablePassthrough(),
  "context": retriever,
} | prompt | model | StrOutputParser()

chain.invoke("Langchainちぇーんの概要を教えて")
