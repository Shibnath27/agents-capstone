from src.tools.zabbix_tool import get_alert
from src.agent.planner import Planner
from src.agent.executor import Executor

def run_demo():
    alert = get_alert()
    print("=== ALERT ===")
    print(alert)
    planner = Planner()
    plan = planner.create_plan(alert)
    print("Plan:", plan)
    executor = Executor()
    result = executor.execute_plan(plan)
    print("Result:", result)
    # Human-in-the-loop: print recommended action
    print("\nRecommended action:", result.get("diagnosis"))
    print("To perform action, operator must approve (simulated).")

if __name__ == "__main__":
    run_demo()
