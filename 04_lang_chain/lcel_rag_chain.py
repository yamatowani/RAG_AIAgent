from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import GitLoader

def file_filter(file_path: str) -> bool:
    return file_path.endswith(".mdx")

loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./langchain",
    branch="master",
    file_filter=file_filter,
)
raw_docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma.from_documents(docs, embeddings)

retriever = db.as_retriever()

prompt = ChatPromptTemplate.from_template('''\
以下の文脈だけを踏まえて質問に回答してください                                      
文脈: """
{context}
"""
質問: {question}
''')

model = ChatOpenAI(model_name="gpt-4o", temperature=0)

query = "AWSのS3からデータを読み込むためのDocument Loaderはありますか？"

chain = (
  {"context": retriever, "question": RunnablePassthrough()}
  | prompt
  | model
  | StrOutputParser()
)

output = chain.invoke(query)
print(output)
