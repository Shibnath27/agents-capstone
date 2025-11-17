"""Gemini LLM client template.

This is a template showing how you might call Gemini (server-side) in a simple wrapper.
**Do not** put API keys into the repo. Instead set environment variables, e.g.

export GEMINI_API_KEY="your_key_here"

Replace the `call_gemini` internals with the actual client code or HTTP request required by the Gemini API version you use.
See official Gemini API documentation for up-to-date instructions.

This file is provided as a template only.
"""
import os
def call_gemini(prompt: str, max_tokens: int = 512) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment. Set it before running with Gemini.")
    # Example placeholder: construct request body (this is NOT a working request)
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens
    }
    # TODO: Replace the following with the actual HTTP call using requests or an official SDK.
    # For example, using requests:
    # resp = requests.post("https://api.gemini.example/v1/generate", json=payload, headers={"Authorization": f"Bearer {api_key}"})
    # return resp.json()["output_text"]
    print("[Gemini] This is a template. Replace with real API call.")
    return "GEMINI_MOCK_RESPONSE"
