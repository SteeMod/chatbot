import openai
import os

# Set your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

def chatbot():
    print("Welcome to the OpenAI Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print("Generating response...")
        response = generate_response(user_input)
        print(f"OpenAI: {response}")

if __name__ == "__main__":
    chatbot()
