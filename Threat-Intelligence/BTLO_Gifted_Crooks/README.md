# BTLO Investigation: Gifted Crooks (MISP & Threat Intelligence)

![Platform](https://img.shields.io/badge/Platform-Blue%20Team%20Labs%20Online-blue)
![Category](https://img.shields.io/badge/Category-Threat%20Intel%20%2F%20MISP-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Status](https://img.shields.io/badge/Status-Completed%20100%25-brightgreen)

## 📋 Scenario Overview
This investigation focuses on analyzing an incident event (`ID: 10128`) logged within the **MISP (Malware Information Sharing Platform)**. The goal is to perform threat intelligence extraction, parse IOCs (Indicators of Compromise), identify dropper artifacts, extract C2 infrastructure, and perform IP enrichment.

* **Alert Source:** CERT-UA (Ukraine)
* **Campaign Type:** Cyber Espionage (UAC-0226)
* **TLP Rating:** `TLP:CLEAR`

---

## 🛠️ Tools & Technologies Used
* **MISP (Malware Information Sharing Platform)** — Attribute filtering, correlation analysis, and object parsing.
* **CyberChef** — Data defanging and format conversion.
* **IP Lookup / Geolocation Tools** — Enrichment of C2 infrastructure.

---

## 🔍 Key Findings & Analysis

1. **Threat Actor Activity:** The alert originates from CERT-UA regarding target cyber espionage activity (UAC-0226) directed at innovation centers and government entities.
2. **Initial Access & Delivery:** The threat campaign relies on malicious document delivery (Excel documents with macros) accompanied by PowerShell scripts (`kgbkewfu32mm.ps1`, `mnmth.ps1`).
3. **Artifact Dropped:** An initial execution archive `status.zip` was dropped into the directory `%TEMP%\empzyqv5I0q\`.
4. **C2 Infrastructure:** 
* Primary C2: `89[.]44[.]9[.]138:3240` (Geolocated to France)
* Secondary C2: `37[.]120[.]239[.]137:8081` (Geolocated to Netherlands)

---

## ❓ Investigation Questions & Answers

| # | Question | Answer |
|---|---|---|
| **Q1** | Country issuing the alert & campaign type | `Ukraine, Cyber Espionage` |
| **Q2** | Published date & creator organization | `2025-04-08 08:43:37, rost.cert.ua` |
| **Q3** | Total Attributes and Objects count | `56, 21` |
| **Q4** | Unique attribute categories count | `4` |
| **Q5** | Unique file extension IOCs (alphabetical) | `.ps1, .xlsm, .zip` |
| **Q6** | Total number of office documents | `9` |
| **Q7** | Script filenames (alphabetical) | `kgbkewfu32mm.ps1, mnmth.ps1` |
| **Q8** | Dropped initial artifact filename & path | `status.zip, %TEMP%\empzyqv5I0q\` |
| **Q9** | First C2 IP and Port (defanged) | `89[.]44[.]9[.]138, 3240` |
| **Q10**| Second C2 IP and Port (defanged) | `37[.]120[.]239[.]137, 8081` |
| **Q11**| First C2 country (ICANN IP Lookup) | `France` |
| **Q12**| Second C2 country (ICANN IP Lookup) | `Netherlands` |
| **Q13**| TLP tag assigned to event | `TLP:CLEAR` |

---

## 🎯 Conclusion & Key Takeaways
Navigating MISP efficiently requires a combination of structured filtering and precise attribute mapping. Distinguishing between raw network indicators and correlated C2 objects is essential for accurate threat analysis and IOC enrichment during real-world SOC investigations.
