from openai import OpenAI
from app.config import ENVIRONMENTS



APIKEY = ENVIRONMENTS['openai_token']

client = OpenAI(
    api_key=APIKEY
)

MODEL="gpt-3.5-turbo"
MAXTOKENS = 1000

def openai_controller(SYSTEM_THINKING):
    try:
        completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_THINKING},
            {"role": "user", "content": "comienza ahora"}
        ]
    )
        # print(completion.choices[0].message)
        return completion.choices[0].message.content
    except Exception as e:
        print(e)