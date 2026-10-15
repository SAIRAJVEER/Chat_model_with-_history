from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain_mistralai import ChatMistralAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage

model = ChatMistralAI(model="ministral-3b-2512")
message = [SystemMessage(content="You are a like a teacher who explain thing like explaining to a kid.")]
while True:
    prompt = input("User: ")
    if prompt.lower() == "exit":
        break
    message.append(HumanMessage(content=prompt))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ", response.content)

print("Message history:", message)