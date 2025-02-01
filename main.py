import os
from openai import OpenAI

class OpenRouterChatBot:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )
        self.conversation_history = []
        self.system_prompt = {
            "role": "system",
            "content": "You are a helpful assistant. Keep responses concise and friendly."
        }
        
    def chat(self):
        print("Chatbot activated! Type 'exit' to quit.")
        self.conversation_history.append(self.system_prompt)
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
                
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            try:
                completion = self.client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "https://your-domain.com",
                        "X-Title": "My Chatbot"
                    },
                    model="openai/gpt-3.5-turbo",
                    messages=self.conversation_history
                )
                
                response = completion.choices[0].message.content
                print(f"Bot: {response}")
                
                self.conversation_history.append({
                    "role": "assistant",
                    "content": response
                })
                
            except Exception as e:
                print(f"Error: {str(e)}")
                break

if __name__ == "__main__":
    bot = OpenRouterChatBot()
    bot.chat()