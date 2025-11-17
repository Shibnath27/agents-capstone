from src.tools.zabbix_tool import get_alert
from src.tools.log_retriever import fetch_recent_logs
from src.tools.proxmox_tool import query_vm
from src.llm.llm_client import call_llm

class Executor:
    def __init__(self):
        pass

    def execute_plan(self, plan):
        outputs = {}
        for step in plan.get("steps", []):
            action = step.get("action")
            args = step.get("args", {})
            if action == "fetch_logs":
                outputs["logs"] = fetch_recent_logs(args.get("service","nginx"), args.get("minutes",15))
            elif action == "query_vm":
                outputs["vm"] = query_vm(args.get("vm_id","vm-101"))
            elif action == "summarize":
                prompt = f"Summarize logs and vm info for diagnosis. logs: {outputs.get('logs')[:1000]} vm: {outputs.get('vm')}"
                outputs["diagnosis"] = call_llm("diagnose: "+prompt)
        return outputs
