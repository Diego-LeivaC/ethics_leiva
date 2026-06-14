# This module provides an interface for interacting with Mistral and Gemma3 through Ollama. 
# It initializes the selected model, sends prompts using the chat API, 
# handles possible execution errors, and returns the generated response.

import ollama

class LLMInterface:

    def __init__(self, model="mistral"):
        self.model = model
        print(f"Using model: {self.model}")

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}])

            return response["message"]["content"]

        except Exception as e:
            print(f"Error generating response: {e}")
            return None