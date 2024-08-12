import openai

# Set your OpenAI API key
api_key = 'your_openai_api_key'

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def chatbot():
    print("Welcome to the OpenAI Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"OpenAI: {response}")

if __name__ == "__main__":
    chatbot()
