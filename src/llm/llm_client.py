"""Simple LLM client wrapper.
No API keys here — keep keys in env vars if you choose to run with a real provider.
This wrapper provides `call_llm(prompt, max_tokens=...)` returning text.
"""
import os
def call_llm(prompt: str, max_tokens: int = 512) -> str:
    # MOCK: simple deterministic response for demo purposes.
    # Replace with real LLM call (OpenAI/Gemini) for production.
    print("[LLM] prompt:", prompt[:200].replace("\n"," "))
    # Very basic heuristic mock:
    if "plan" in prompt.lower():
        return '{"steps":[{"action":"fetch_logs","args":{"minutes":15}}, {"action":"query_vm","args":{"vm_id":"vm-101"}}, {"action":"summarize","args":{}}]}'
    if "diagnose" in prompt.lower():
        return "Likely cause: nginx service OOM due to memory spike. Recommend restart nginx and monitor."
    return "MOCK_RESPONSE"
