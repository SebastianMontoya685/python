#!usr/bin/env python3

tasks = ["Backup", "Security Scan", "System Update", "Cleanup"]
statuses = ["Done", "Failed", "Done", "Pending"]

for i, (task, status) in enumerate(zip(tasks, statuses)):
    dot_count = 20 - len(task)
    dots = "." * dot_count
    print(f"[{i}] {task} {dots} {status}")