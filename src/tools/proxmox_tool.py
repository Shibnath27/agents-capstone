"""Mock Proxmox client returning VM state for demo."""
def query_vm(vm_id: str):
    # demo static response
    return {
        "vm_id": vm_id,
        "cpu": "3.2",
        "mem_percent": 82,
        "disk_percent": 43,
        "status": "running",
        "last_boot": "2025-11-01T10:12:00"
    }
