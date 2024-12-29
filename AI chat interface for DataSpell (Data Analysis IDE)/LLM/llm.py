import openai
import os

class LLM:
    def __init__(self, api_key_file="api_key.txt", prompt_file="prompt_template.txt", model="gpt-4o-mini"):
        self.api_key = self._load_file(api_key_file)
        self.prompt_template = self._load_file(f'prompts/{prompt_file}')
        if not self.api_key:
            raise RuntimeError("API key not found! Ensure the key is in the file.")
        
        self.model = model
        self.client = openai.OpenAI(api_key=self.api_key) 


    @staticmethod
    def _load_file(file_path):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_path)
        with open(file_path, "r") as file:
            return file.read().strip()

    def generate_response(self, user_input):
        user_prompt = f'Input: {user_input}';
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "developer", "content": self.prompt_template},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()


if __name__ == "__main__":
    llm = LLM()
    user_input = "Filter rows where age > 30 and select the 'name' column."
    print(llm.generate_response(user_input))
