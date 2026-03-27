import re
from collections import defaultdict

# Sample log file path
LOG_FILE = "data/sample_logs.txt"

# Detection threshold
THRESHOLD = 5


def parse_logs(file_path):
    """Read logs and extract failed SSH attempts by source IP."""
    ip_attempts = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if "Failed password" in line and match:
                    ip = match.group(1)
                    ip_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
        return {}

    return ip_attempts


def detect_bruteforce(ip_attempts):
    """Detect brute force attempts based on threshold."""
    alerts = []

    for ip, count in ip_attempts.items():
        if count >= THRESHOLD:
            alerts.append({
                "event_type": "Brute Force Attack",
                "source_ip": ip,
                "attempt_count": count,
                "severity": "HIGH"
            })

    return alerts


def generate_ai_summary(alert):
    """Simulate AI-generated incident summary."""
    return f"""
Incident Type: {alert['event_type']}

Summary:
Multiple failed SSH login attempts were detected from IP address {alert['source_ip']}.

Analysis:
The pattern indicates a brute force attack attempting unauthorized access.

Severity: CRITICAL

Recommended Actions:
- Block the source IP immediately
- Review authentication logs
- Enforce stronger password policies
- Enable multi-factor authentication
"""


def main():
    print("Reading logs...")
    ip_attempts = parse_logs(LOG_FILE)

    if not ip_attempts:
        print("No failed login attempts found.")
        return

    alerts = detect_bruteforce(ip_attempts)

    if not alerts:
        print("No brute force attacks detected.")
        return

    print("\nDetected Alerts:")
    for alert in alerts:
        print(alert)
        print(generate_ai_summary(alert))


if __name__ == "__main__":
    main()
