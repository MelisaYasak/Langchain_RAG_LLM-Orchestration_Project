from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.1)

messages = [{
    SystemMessage(content="Translate the following from English to Turkish"),
    HumanMessage(content="hi!"),
}]
parser = StrOutputParser()

#response = model.invoke(messages)
chain = model | parser

if __name__ == "__main__":
     print(chain.invoke(messages))