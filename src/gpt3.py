import openai
from pathlib import Path
openai.api_key = Path('resources/openai_config.txt').read_text().strip()


class Engine:
    def __init__(self):
        self.prompt = Path('resources/prompt.txt').read_text()

        self.params = {
            'engine': 'davinci',
            'max_tokens': 10,
            'temperature': 0.0,
            'stop': [']','\n']
        }

    def __call__(self, text):
        text = text.replace('\n\n', '\n').replace('\n\n', '\n').replace('\n\n', '\n')
        prompt = self.prompt + '\n' + text + '\n['

        f = lambda r: (r['choices'])[0]['text']
        response = f(openai.Completion.create(prompt=prompt, **self.params))
        return response