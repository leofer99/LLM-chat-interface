import os
from openai import OpenAI
from together import Together
import tiktoken

MODEL = "meta-llama/Llama-3.3-708-Instruct-Turbo-Free"
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."


class ConversationManager:
    def __init__(self, model=MODEL, system_prompt=SYSTEM_PROMPT, temperature=0.7, max_tokens=100, token_budget=100):

        api_key
        api_key = os.getenv("TOGETHER_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.client = Together()

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.encoding = self.get_encoding(self.model)


    def get_encoding(self, model):
        #encoder for counting tokens - can be model specific
        try:
            return tiktoken.encoding_for_model(model)
        except KeyError:
            print(f"Warning: Tokenizer for model '{model}' not found. Using cl100k_base encoding.")
            return tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text):
        return len(self.encoding.encode(text))

    def total_tokens_used(self):
        try:
            return sum(self.count_tokens(message["content"]) for message in self.messages) + 4 * len(self.messages) + 2
        except Exception as e:
            print(f"Error counting tokens: {e}")
            return 0
        
    def enforce_token_budget(self):
        try:
            while self.total_tokens_used() > self.token_budget:
                if len(self.messages) <= 2:
                    break
                # Remove the oldest user or assistant message, but keep the system prompt
                self.messages.pop(1)

        except Exception as e:
            print(f"Token budget error: {e}")


    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        self.enforce_token_budget()

        # connecting to the chat
        response = self.client.chat.completions.create(
            model = self.model,
            messages = self.messages,
            temperature = self.temperature, #temperature controls randomness of output
            max_tokens = self.max_tokens, #limit length of tokens in output (reply)
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})

        return reply
    


if __name__ == "__main__":
    manager = ConversationManager()

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            break
        answer = manager.chat(user_input)

        print("You:", user_input)
        print("Assistant:", answer)
        print(f"Current tokens: {manager.total_tokens_used()}")

        
#TO DO:
#Add reference notes (sources)
#Persistence between sessions (add files to working directory)

