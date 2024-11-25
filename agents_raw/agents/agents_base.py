import os
import requests
import json
from typing import List
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama  # type: ignore
from dotenv import load_dotenv

# from bs4 import BeautifulSoup
# from IPython.display import Markdown, display, update_display
from abc import ABC, abstractmethod
from openai import OpenAI
from loguru import Logger


load_dotenv("../.env")

MODEL = "gpt-4o-mini"
openai = OpenAI()


class AgentBase(ABC):
    def __init__(self, name: str, max_retries: int = 2, verbose: bool = True):  # name is agent name
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_openai(self, messages, temprature=0.7, max_tokens=150):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    Logger.info(f"[{self.name}] sending message to AI server")
                    for msg in messages:
                        Logger.debug(f"{msg["role"]}: {msg["content"]}")
                completion = openai.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    temperature=temprature,
                    max_tokens=max_tokens,
                )
                result = completion.choices[0].message
                if self.verbose:
                    Logger.info(
                        f"[{self.model}] received response from AI server: {result}")

                return result
            except Exception as e:
                retries += 1
                if self.verbose:
                    Logger.error(f"{self.name} Failed to call OpenAI: {e}")
                raise Exception(f"{self.name} Failed")
