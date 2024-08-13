import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

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
