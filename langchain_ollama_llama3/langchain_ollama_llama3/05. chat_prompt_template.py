from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
    ("user", "{user_input}"),
])
# chat_prompt = ChatPromptTemplate.from_messages(
#     [
#         SystemMessagePromptTemplate.from_template("이 시스템은 천문학 질문에 답변할 수 있습니다."),
#         HumanMessagePromptTemplate.from_template("{user_input}"),
#     ]
# )

llm = Ollama(model="llama3:latest")

chain = chat_prompt | llm | StrOutputParser()

print(chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"}))
