import openai
# import openai_secret_manager

from .FewShotDaVinci import prompt, Teacher, Student, Subject

# secrets = openai_secret_manager.get_secret("openai")
# api_key = secrets["api_key"]


api_key = "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"
openai.api_key = api_key

while True:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=150,
        n=1,
        # frequency_penalty=0,
        # presence_penalty=0.6,
        stop=[f"{Teacher.name}:", f"{Student.name}:"],

    )
    print(prompt + response.choices[0].text)
    user_response = f"\n{Student.name}: {input(f'{Student.name}: ')}\n{Teacher.name}: "
    prompt += response.choices[0].text + user_response
