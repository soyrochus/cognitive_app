
from typing import AsyncIterable, Iterable
from cognitive_api.services import ollama
from cognitive_api.services.requests import PromptRequest
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from cognitive_api.services.ollama import send_prompt, send_prompt_dummy
from fastapi import APIRouter

router = APIRouter()

@router.post("/prompt")
async def prompt_endpoint(request_body: PromptRequest) -> StreamingResponse:
    try:
        # Create a generator object
        generator = send_prompt(ollama, request_body.prompt)
        #generator = send_prompt_dummy(ollama, request_body.prompt)

        # Define a generator function to pass to StreamingResponse
        def iter_wrapper() -> AsyncIterable[str]: # type: ignore
            for response in generator:
                yield response

        # Return the streaming response using the wrapper generator
        return StreamingResponse(iter_wrapper(), media_type="text/plain") # type: ignore
    except Exception as e:
        # Basic error handling
        raise HTTPException(status_code=500, detail=str(e))


