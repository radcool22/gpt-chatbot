import openai

openai.api_key = "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"

def main(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = main(user_input)
        print("Chatbot: " + response)