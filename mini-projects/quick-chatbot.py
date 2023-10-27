import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = []

def chat_with_gpt(prompt, language="en"):
  conversation_history.append({"role": "user", "content": prompt})
  # Translate user input to English if the input is in Spanish
  if language == "es":
      translated_input = translate_to_english(prompt)
      conversation_history[-1]["content"] = translated_input
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation_history
  )
  conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
  return response.choices[0].message.content.strip()

def translate_to_english(text):
  translated_text = translate_to_english_using_external_service(text)
  return translated_text

def translate_to_english_using_external_service(text):
    return "This is a sample translation to English."

if __name__ == "__main__":
  while True:
    user_input = input("You (es/en): ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break

    language = user_input.lower()
    user_input = input("You: ")  # Prompt the user for input

    try:
      response = chat_with_gpt(user_input, language)
    except Exception as e:
        print("An error occurred:", str(e))
        response = "I'm sorry, I encountered an error."
    
    print(f"Chatbot ({language}):", response)
