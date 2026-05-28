# Active Directory Attack Lifecycle Mapping

## 🎯 Lab Objective
To simulate an internal network compromise by moving from an unauthenticated network position to full Domain Admin dominance within a Windows Active Directory environment.



## 🛠️ Tools Used
* Netexec / CrackMapExec
* BloodHound & SharpHound
* Impacket Suite (`GetNPUsers.py`, `secretsdump.py`)
* Mimikatz

## ⚔️ Attack Execution Timeline

[Initial Foothold] ──> [LLMNR/NBT-NS Poisoning] ──> [BloodHound Recon] ──> [Kerberoasting] ──> [Domain Admin]

1. **Internal Enumeration & Poisoning:** Leveraged Responder to capture NetNTLMv2 hashes via LLMNR poisoning. Hashes were cracked offline using `Hashcat` with the RockYou wordlist.
2. **Domain Reconnaissance:** Executed `SharpHound.exe` to collect active directory object relationships. The data was visualized in **BloodHound**, revealing a shortest path to Domain Admin via an over-privileged service account.
3. **Kerberoasting:** Used Impacket's `GetUserSPNs.py` to request Service Principal Names (SPNs) for the targeted service account. The ticket was cracked locally to reveal the plaintext service account password.
4. **Lateral Movement & Domain Dominance:** Authenticated via SMB to the Domain Controller using the compromised service credentials. Executed `secretsdump.py` to dump the NTDS.dit database, capturing the NTLM hash of the Domain Administrator.

🛡️ Defensive Remediation & Hardening

* **Disable Legacy Protocols:** Disabled LLMNR and NBT-NS network-wide via Group Policy (GPO) and enforced SMB Signing to neutralize man-in-the-middle poisoning attacks.
* **Kerberoasting Mitigation:** Enforced a minimum 25-character password policy for all Service Principal Names (SPNs) and transitioned high-privilege service accounts to Group Managed Service Accounts (gMSAs) to prevent offline brute-forcing.
* **Tiered Administration:** Implemented an Active Directory Administrative Tiering Model (Tier 0/1/2) to ensure Domain Admin credentials are never cached on workstations or servers where service accounts can access them.
