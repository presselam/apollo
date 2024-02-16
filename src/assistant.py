from openai import OpenAI


class Assistant:
    def __init__(self, model: str = None, system: str = None):
        self.client = OpenAI()
        self.model = model or "gpt-3.5-turbo"
        self.system = system or "you are a source code generator"
        self.messages = [
            {"role": "system", "content": self.system},
        ]

    def chat(self, prompt: str, commit: bool = True) -> str:
        self.messages.append({"role": "user", "content": prompt})

        answer = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
            + "qui officia deserunt mollit anim id est laborum."
        )

        if commit:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
            )
            answer = response.choices[0].message.content

        self.messages.append({"role": "assistant", "content": answer})

        return answer
