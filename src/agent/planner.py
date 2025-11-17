from src.llm.llm_client import call_llm
import json

class Planner:
    def __init__(self):
        pass

    def create_plan(self, alert):
        prompt = f"""You are an agent planner. Create a structured JSON plan for investigating this alert:
{alert}
Return JSON only with steps array where each step is {{action:..., args:...}}."""
        raw = call_llm(prompt)
        try:
            plan = json.loads(raw)
        except Exception:
            # fallback simple plan
            plan = {"steps":[{"action":"fetch_logs","args":{"minutes":15}},{"action":"query_vm","args":{"vm_id":"vm-101"}},{"action":"summarize","args":{}}]}
        return plan
