#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

import requests
from typing import Iterator, NamedTuple
import json


class LLM(NamedTuple):
    llm: str  # The name of the LLM model, e.g., "llama2"
    url: str  # The URL of the Ollama instance, e.g., "http://localhost:11434"


def send_prompt_dummy(llm: LLM, prompt: str) -> Iterator[str]:
    """Emulate send_prompt"""
    yield "Once upon a time, there was a dragon"
    yield "It was a fearsome creature, with scales as hard as steel and breath as hot as fire."
    yield "It lived in a cave at the top of a mountain, and it was the terror of the entire kingdom."
    yield "The people lived in fear of the dragon, and they prayed for a hero to come and slay the beast."
    yield "One day, a brave knight appeared, armed with a sword and a shield. He climbed the mountain and"
    yield "entered the cave, where he found the dragon sleeping. The knight raised his sword and struck"
    yield "the dragon, but the dragon woke up and roared. The knight fought bravely, "
    yield "but the dragon was too powerful. Just when it seemed that all was lost, the knight remembered"
    yield "a story he had heard about a magical amulet that could control dragons. He reached into his "
    yield "pocket and pulled out the amulet, and the dragon stopped attacking. The knight used the amulet "
    yield "to command the dragon to leave the kingdom and never return. The dragon obeyed, and the people "
    yield "rejoiced. From that day on, the knight was known as the Dragon Slayer, and he was hailed as a hero."
    yield "The end."

def send_prompt(llm: LLM, prompt: str) -> Iterator[str]:
    """
    Sends a prompt to the specified LLM model hosted by an Ollama instance and yields the response line by line.

    This function sends a POST request to the Ollama instance with a JSON payload containing the model name and the prompt.
    The Ollama instance generates a response based on the prompt and the model, and sends it back as a stream of JSON objects.
    Each JSON object has a 'response' field that contains a piece of the generated text.
    This function yields these pieces of text one by one, giving the appearance of the text being generated in real time.

    Args:
        llm (LLM): An LLM namedtuple containing the model name and the URL of the Ollama instance.
            The model name should be a string that identifies the model to use for generation.
            The URL should be a string that specifies the location of the Ollama instance.

            For example, if you have an Ollama instance running at 'http://localhost:8000' and you want to use the 'mistral' model,
            you would create an LLM namedtuple like this: LLM(llm='mistral', url='http://localhost:8000').

        prompt (str): The prompt to send to the LLM.
            This should be a string that you want the model to generate a response to.
            For example, if you want to generate a story about a dragon, you might use the prompt 'Once upon a time, there was a dragon'.

    Yields:
        str: The generated text, piece by piece.
            Each piece of text is a string that was contained in the 'response' field of a JSON object in the response from the Ollama instance.
            These pieces of text are yielded in the order they are received, so they should form a coherent piece of text when concatenated.

    Raises:
        Exception: If the request to the Ollama instance fails, an exception is raised with a message indicating the status code of the response.
    """
    # Define the endpoint for generating responses
    endpoint = f"{llm.url}/api/generate"

    # Prepare the data payload for the POST request
    data = {
        "model": llm.llm,
        "prompt": prompt
    }

    # Send the POST request and capture the response
    response = requests.post(endpoint, json=data, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Yield the generated text from the response line by line
        for line in response.iter_lines():
            if line:  # filter out keep-alive new lines
                decoded_line = line.decode('utf-8')
                json_line = json.loads(decoded_line)
                response_line: str = json_line.get('response')
                if response_line is not None:
                    yield response_line
    else:
        # Handle possible errors
        yield f"Error: Received status code {response.status_code}"


# Example usage:
if __name__ == "__main__":
    # Define the LLM and URL
    my_llm = LLM(llm="codellama:7b", url="http://localhost:11434")

    # Define the prompt
    my_prompt = "what is an implementation for fibonacci in python. Then compare it with one in Rust"

    # Send the prompt and print the response
    for response in send_prompt(my_llm, my_prompt):
        print(response, end="")
