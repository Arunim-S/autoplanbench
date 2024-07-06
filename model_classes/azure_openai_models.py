from typing import List, Union
# from azure.ai.textanalytics import TextAnalyticsClient
from openai import AzureOpenAI
from .llm_models import LLMModel
from pydantic import BaseModel
import json

import os

client = AzureOpenAI(
  azure_endpoint = "https://gpt4-turbo-norway-docu3c.openai.azure.com/", 
  api_key="cfa86d760960466f862ec633aa9bdc6d",  
  api_version="2023-12-01-preview"
)

class AzureChatModel(LLMModel):
    def __init__(self,
                 model_name: str,
                 model_path: str,
                 max_tokens: int,
                 temp: float,
                 max_history: Union[int, None],
                 cache_directory: Union[str, None] = None):
        super().__init__(model_name=model_name, model_path=model_path, max_tokens=max_tokens,
                    temp=temp, max_history=max_history, cache_directory=cache_directory)

    def init_model(self, init_prompt: str):
        self.initial_prompt = init_prompt
        self.history.append({"role": "system", "content": self.initial_prompt})
        self.initial_history = [{"role": "system", "content": self.initial_prompt}]
        self.role_user = "user"
        self.role_assistant = "assistant"

    def update_init_prompt(self, new_init_prompt: str):
        # need to adapt self.initial_prompt, self.history and self.initial_history
        self.initial_prompt = new_init_prompt
        self.initial_history[0]["content"] = new_init_prompt
        self.history = self.initial_history.copy()

    def add_examples(self, examples: List[dict]) -> None:
        """
        Add the examples from the input list to the dialogue history
        :param examples: list of examples, where each example is of the form:
                        {'role': 'user', 'content': content} or {'role': 'assistant', 'content': content}
        :return:
        """
        for example in examples:
            role_type = example['role']
            if role_type == 'user':
                role = self.role_user
            elif role_type == 'assistant':
                role = self.role_assistant
            else:
                raise ValueError
            content = example['content']
            self.history.append({"role": role, "content": content})
        self.initial_history = self.history.copy()

    def get_history(self) -> List[dict]:
        return self.history

    def get_initial_history(self) -> List[dict]:
        return self.initial_history

    def reset_history(self):
        self.history = self.initial_history.copy()

    def update_history(self, new_history: List[dict]):
        self.history = new_history.copy()


    def _generate(self, prompt: str):
        output = client.chat.completions.create(model=self.model_path, messages=self.history, temperature=self.temp, max_tokens=self.max_tokens)
        output = output.model_dump()
        response = output['choices'][0]['message']['content']
        self.update_token_counts(output['usage'])

        return response

    def update_token_counts(self, usage_dict: dict):
        """
        Update the processed token counts based on the information returned by the Chat model
        :param usage_dict:
        :return:
        """
        self.total_input_tokens += usage_dict['prompt_tokens']
        self.total_output_tokens += usage_dict['completion_tokens']
        self.total_tokens += usage_dict['total_tokens']
        self.max_input_tokens = usage_dict['prompt_tokens'] if usage_dict['prompt_tokens'] > self.max_input_tokens else self.max_input_tokens
        self.max_output_tokens = usage_dict['completion_tokens']  if usage_dict['completion_tokens'] > self.max_output_tokens else self.max_output_tokens
        self.max_total_tokens = usage_dict['total_tokens'] if usage_dict['total_tokens'] > self.max_total_tokens else self.max_total_tokens

    def create_cache_query(self, prompt: str):
        # put together everything that is in the chat history (this already includes the prompt)
        query = ''
        for entry in self.history:
            for role, content in entry.items():
                query += f'{role}: {content} // '
        return query

    def prepare_for_generation(self, user_message) -> str:

        self.history.append({"role": self.role_user, "content": user_message})

        return user_message

    def clean_up_from_generation(self, model_response) -> str:
        # add the generated response to the history
        self.history.append({"role": self.role_assistant, "content": model_response})

        return model_response

class AzureComplModel:
    def __init__(self,
                 model_name: str,
                 model_path: str,
                 max_tokens: int,
                 temp: float,
                 max_history: Union[int, None],
                 cache_directory: Union[str, None] = None):
        self.model_name = model_name
        self.model_path = model_path
        self.max_tokens = max_tokens
        self.temp = temp
        self.max_history = max_history
        self.cache_directory = cache_directory
        self.initial_prompt = None

    def init_model(self, init_prompt: str):
        self.initial_prompt = init_prompt

    def update_init_prompt(self, new_init_prompt: str):
        self.initial_prompt = new_init_prompt

    def get_initial_history(self):
        return [{'system': self.initial_prompt}]

    def get_history(self) -> List[dict]:
        return [{"system": self.initial_prompt}]

    def reset_history(self):
        pass

    def update_history(self, new_history: List[dict]):
        pass

    def _generate(self, prompt: str):
        # Here, you would call Azure's Completion API to generate a response based on the prompt
        # Replace this with the appropriate Azure API call
        response = "Placeholder response from Azure's Completion API"
        return response

    def create_cache_query(self, prompt: str):
        return prompt

    def prepare_for_generation(self, user_message) -> str:
        prompt = self.initial_prompt + '\n\n' + user_message
        return prompt

    def clean_up_from_generation(self, model_response) -> str:
        return model_response
