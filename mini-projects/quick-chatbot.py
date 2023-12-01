import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = []

def chat_with_gpt(prompt):
  conversation_history.append({"role": "user", "content": prompt})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation_history
  )
  conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
  return response.choices[0].message.content.strip()

# Add code to translate English to Spanish here

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break

    try:
      response = chat_with_gpt(user_input)
    except Exception as e:
        print("An error occurred:", str(e))
        response = "I'm sorry, I encountered an error."
    
    print("Chatbot: ", response)
