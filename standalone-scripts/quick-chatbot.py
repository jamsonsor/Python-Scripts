import openai
import os

openai.api_key = "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" #os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )

  return response.choices[0].message.content.strip()

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break

    response = chat_with_gpt(user_input)
    print("Chatbot: ", response)
