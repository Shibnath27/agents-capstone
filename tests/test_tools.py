from src.tools.zabbix_tool import get_alert
from src.tools.log_retriever import fetch_recent_logs
from src.tools.proxmox_tool import query_vm

def test_get_alert():
    a = get_alert()
    assert 'id' in a

def test_fetch_logs():
    logs = fetch_recent_logs('nginx', 15)
    assert isinstance(logs, str)

def test_query_vm():
    vm = query_vm('vm-101')
    assert vm['vm_id'] == 'vm-101'
