import os
import json
import requests

import openai
from django.conf import settings

class OpenAIUtils:

    openai.api_key = settings.OPENAI_API_KEY
    #CHAT_MODEL = "text-davinci-003"
    CHAT_MODEL = "gpt-3.5-turbo"
    #EMBEDDING_MODEL = "ada-002"
    @staticmethod
    def simple_answer(question):
        msg = [{"role": "user", "content": question}]
        #completion = openai.Completion.create(model=OpenAIUtils.CHAT_MODEL, prompt=question)
        completion = openai.ChatCompletion.create(model=OpenAIUtils.CHAT_MODEL, messages = msg)
        answer = completion.choices[0].message["content"]
        return answer
