import pickle
import uuid

from openai import OpenAI

from configuration import Configuration

CONFIG = Configuration()


class Assistant:
    def __init__(self, model: str = None, system: str = None):
        self.client = OpenAI()
        self.chat_id = str(uuid.uuid4())
        self.model = model or "gpt-3.5-turbo"
        self.system = system or "you are a source code generator"
        self.messages = [
            {"role": "system", "content": self.system},
        ]

    def historyId(self):
        return self.chat_id

    def loadHistory(self, id: str):
        self.chat_id = id
        try:
            with open(f"{CONFIG.history_dir}/{self.chat_id}", "rb") as fh:
                self.messages = pickle.load(fh)
            return True
        except FileNotFoundError:
            return False

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

        with open(f"{CONFIG.history_dir}/{self.chat_id}", "wb") as fh:
            pickle.dump(self.messages, fh)

        return answer
