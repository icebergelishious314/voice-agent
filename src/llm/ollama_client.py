# src/llm/ollama_client.py

import requests

OLLAMA_CHAT_URL = "http://127.0.0.1:11434/api/chat"
OLLAMA_GEN_URL = "http://127.0.0.1:11434/api/generate"


def ollama_respond(model: str, messages: list[str]) -> str:
    """
    Model-agnostic Ollama response function.
    Uses /api/chat if available, falls back to /api/generate.
    """

    # Try chat API first
    try:
        payload = {
            "model": model,
            "messages": messages,
            "stream": False
        }
        r = requests.post(
            OLLAMA_CHAT_URL,
            json=payload,
            timeout=120
        )
        if r.status_code == 200:
            return r.json()["message"]["content"]
    except Exception:
        pass

    # Fallback to generate API
    prompt = ""
    for m in messages:
        role = m["role"].upper()
        prompt += f"{role}: {m['content']}\n"
    prompt += "ASSISTANT:"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(
        OLLAMA_GEN_URL,
        json=payload,
        timeout=120
    )
    r.raise_for_status()

    return r.json()["response"]
