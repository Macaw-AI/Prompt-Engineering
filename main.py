import random

import openai
# import openai_secret_manager

# from FewShots import prompt, teacher, student, location
from SplitIntoTasks import whole_conversation, teacher, student, location, header,ask_for_bullet


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
    transcript_filename = f"Prompt-Engineering/conversations/{location}/{engine}/{random.random()}.txt"
    prompt_to_send = header
    clear_iter = 1
    
    while clear_iter<15:
        save_to_file(whole_conversation, transcript_filename) 
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt_to_send,
            temperature=0.8,
            max_tokens=150,
            n=1,
            # frequency_penalty=0,
            # presence_penalty=0.6,
            stop=[f"{teacher.name}:", f"{student.name}:"],
        )
        print(response.choices[0].text[1:])
        user_response = f"\n{student.name}: {input(f'{student.name}: ')}\n{teacher.name}: "
        whole_conversation += response.choices[0].text + user_response
        
        if clear_iter%5==0:
            prompt_to_send = header

        prompt_to_send += response.choices[0].text + user_response
        clear_iter+=1
#        print(f"----------\n{prompt_to_send}\n---------------") #uncomment it to see what prompt looks like
    save_to_file(whole_conversation, transcript_filename)

    # bull_response = openai.Completion.create(
    #     engine=engine,
    #     prompt=ask_for_bullet + whole_conversation,
    #     temperature=0.8,
    #     max_tokens=150,
    #     n=1,
    #     # frequency_penalty=0,
    #     # presence_penalty=0.6,
    #     stop=[f"{teacher.name}:", f"{student.name}:"],)
    # save_to_file(bull_response.choices[0].text,transcript_filename)


    
