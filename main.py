import random

import openai
# import openai_secret_manager

# from FewShots import prompt, teacher, student, location
from SplitIntoTasks import prompt, teacher, student, location


class ENGINE:
    CURIE = "text-curie-001"  # 10 times cheaper, faster
    DAVINCI = "text-davinci-003"  # more accurate


# secrets = openai_secret_manager.get_secret("openai")
# GPT_KEY = secrets["api_key"]
GPT_KEY = "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"
openai.api_key = GPT_KEY


def save_to_file(text, filename):
    with open(filename, "w+") as f:
        f.write(text)


if __name__ == '__main__':
    engine = ENGINE.DAVINCI
    transcript_filename = f"conversations/{location}/{engine}/{random.random()}.txt"

    while True:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=0.8,
            max_tokens=150,
            n=1,
            # frequency_penalty=0,
            # presence_penalty=0.6,
            stop=[f"{teacher.name}:", f"{student.name}:"],

        )
        print(prompt + response.choices[0].text[1:])
        user_response = f"{student.name}: {input(f'{student.name}: ')}\n{teacher.name}: "
        prompt += response.choices[0].text + user_response
        save_to_file(prompt, transcript_filename)  # <- TODO it should save before user response
