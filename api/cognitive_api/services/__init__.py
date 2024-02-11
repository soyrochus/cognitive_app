"""Services for cognitive_api."""

from cognitive_api.services.ollama import LLM

ollama =  LLM(llm="codellama:7b", url="http://localhost:11434")
