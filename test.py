import openai
import os
import openai
import os

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai():
    print("Start chatting with the AI (type 'exit' to stop):")
    messages = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ai_response = response.choices[0].message['content'].strip()
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})

# Call the function to start the chat
chat_with_ai()
def chat_with_ai():
    print("Start chatting with the AI (type 'exit' to stop):")
    messages = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ai_response = response.choices[0].message['content'].strip()
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})

# Start the chat
chat_with_ai()
