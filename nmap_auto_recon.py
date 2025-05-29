import os
from datetime import datetime

# === CONFIG ===
subnet = "10.212.39.0/24"  # Change to your target range
output_dir = os.path.expanduser("~/nmap_logs")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"{output_dir}/nmap_recon_log_{timestamp}.txt"

# === SETUP ===
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# === NMAP SCAN COMMAND ===
command = f"sudo nmap -sS -sV -p- -oN {log_file} {subnet}"
print(f"Running: {command}")
os.system(command)

# === DONE ===
print(f"\n📝 Scan complete. Results saved in:\n{log_file}")
