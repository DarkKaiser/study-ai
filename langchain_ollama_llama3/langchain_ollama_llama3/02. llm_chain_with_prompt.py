from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt
prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")

# model
llm = Ollama(model="llama3:latest")

# output parser
output_parser = StrOutputParser()

# chain 연결 (LCEL)
chain = prompt | llm | output_parser

# chain 호출
response = chain.invoke({"input": "지구의 자전 주기는?"})

print(response)
