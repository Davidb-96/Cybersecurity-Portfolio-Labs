# Active Directory Attack Lifecycle Mapping

## 🎯 Lab Objective
To simulate an internal network compromise by moving from an unauthenticated network position to full Domain Admin dominance within a Windows Active Directory environment.



## 🛠️ Tools Used
* Netexec / CrackMapExec
* BloodHound & SharpHound
* Impacket Suite (`GetNPUsers.py`, `secretsdump.py`)
* Mimikatz

## ⚔️ Attack Execution Timeline

[Initial Foothold] ──> [LLMNR/NBT-NS Poisoning] ──> [Kerberoasting] ──> [BloodHound Recon] ──> [Domain Admin]

1. **Internal Enumeration & Poisoning:** Leveraged Responder to capture NetNTLMv2 hashes via LLMNR poisoning. Hashes were cracked offline using `Hashcat` with the RockYou wordlist.
2. **Domain Reconnaissance:** Executed `SharpHound.exe` to collect active directory object relationships. The data was visualized in **BloodHound**, revealing a shortest path to Domain Admin via an over-privileged service account.
3. **Kerberoasting:** Used Impacket's `GetUserSPNs.py` to request Service Principal Names (SPNs) for the targeted service account. The ticket was cracked locally to reveal the plaintext service account password.
4. **Lateral Movement & Domain Dominance:** Authenticated via SMB to the Domain Controller using the compromised service credentials. Executed `secretsdump.py` to dump the NTDS.dit database, capturing the NTLM hash of the Domain Administrator.
