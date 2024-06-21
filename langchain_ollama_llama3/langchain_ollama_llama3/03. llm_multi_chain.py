from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English.")
prompt2 = ChatPromptTemplate.from_template(
    "explain {english_word} using oxford dictionary to me in Korean."
)

llm = Ollama(model="llama3:latest")

chain1 = prompt1 | llm | StrOutputParser()

chain2 = (
        {"english_word": chain1}
        | prompt2
        | llm
        | StrOutputParser()
)

response = chain2.invoke({"korean_word":"미래"})

print(response)
