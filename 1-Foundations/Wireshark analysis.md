# Traffic Analysis Lab: Packet Inspection

## 🎯 Lab Objective
To analyze a network packet capture (PCAP) to identify anomalous behavior, map network architecture, and extract unencrypted credentials.

## 🛠️ Tools Used
* Wireshark
* tshark (Command-line packet analysis)

## 🔍 Analysis & Findings

### 1. Protocol Breakdown
Using Wireshark's, the traffic baseline consists of:
* **TCP:** 85% of total traffic (primarily HTTP on port 80).
* **DNS:** 10% query traffic.
* **Other:** 5% (ARP, ICMP).

### 2. Suspicious Activity Identified
* **Finding:** Cleartext Credential Harvesting.
* **Filter Used:** `http.request.method == "POST"`
* **Description:** While analyzing stream 4, an unencrypted HTTP POST request was observed heading to a login portal. The credentials were leaked in plaintext within the packet bytes:
  * **Username:** `admin`
  * **Password:** `Password123!`

## 💡 Remediation Strategy
All web authentication traffic must be encrypted using HTTPS (TLS 1.3) to prevent packet sniffing and man-in-the-middle (MITM) credential harvesting.
