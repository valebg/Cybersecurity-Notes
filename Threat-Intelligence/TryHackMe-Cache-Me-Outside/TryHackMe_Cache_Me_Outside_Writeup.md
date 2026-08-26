# TryHackMe: Cache Me Outside — OSINT Writeup

**Author:** Valeri Votman  
**Date:** August 26, 2026  
**Category:** Open Source Intelligence (OSINT) / Digital Forensics  
**Difficulty:** Medium  
**Platform:** [TryHackMe](https://tryhackme.com/)  

---

## Executive Summary

The **Cache Me Outside** challenge on TryHackMe tests an investigator's ability to trace a retired hacker’s online footprint starting from a single conversation screenshot. By applying structured OSINT methodology, cross-platform profiling, Git commit forensics, and Google Dorking, all five identity markers (full name, exposed email, phone number, city, and exact transit station) were identified in **30 minutes** (50% faster than the expected 60-minute duration).

---

## Challenge Overview & Objectives

* **Scenario:** A retired hacker (`JJ ^_^`) left fragments of his identity scattered across public platforms and code repositories.
* **Target Information to Extract:**
  1. Retired hacker's full name
  2. Accidentally exposed email address
  3. Phone number
  4. Current location (City)
  5. Tram station visited on May 7, 2026

---

## Investigation Steps & Methodology

### Step 1: Initial Entry & Profile Correlation
* **Artifact:** Chat screenshot between `WKM1337` and `JJ ^_^`.
* **Lead:** In the chat log, `JJ ^_^` mentions moving away from hacking into outdoor activities and shares a **Komoot** profile link (`/user/5667624959836`).
* **Finding:** Investigating the Komoot account reveals the target's display name, **Jim Lee**, and hints at his personal company and active GitHub repository.

### Step 2: Git Forensics & Email Discovery
* **Target Platform:** GitHub (`jiml33t`)
* **Technique:** Inspecting commit metadata using `.patch` / `.diff` URL manipulation.
* **Execution:**
  1. Located the primary repository `jiml33t/jiml33t` (and `jimleepro1-cell`).
  2. Appended `.patch` to the initial commit URL (`https://github.com/jiml33t/jiml33t/commit/<HASH>.patch`).
  3. Extracted raw header metadata from the `From:` line.
* **Finding:** Exposed Email — `jimleepro1@gmail.com`.

### Step 3: Google Dorking & Active OSINT Analysis
* **Technique:** Targeted Google Dorking using quoted parameters (`"jimleepro1@gmail.com"`, `"jiml33t"`).
* **Finding & Correlation:** 
  * Automated email triggers and indexed data correlated the email to an active contact number: `+40 743 321 239`.
  * Geolocation data tied the target's corporate footprint to **Timișoara, Romania**.
  * Specific transit activity from May 7, 2026, pinpointed the exact stop: **Piața Gheorghe Domășneanu**.

---

## Challenge Answers Summary

| Question | Extracted Artifact / Answer | Methodology Used |
| :--- | :--- | :--- |
| **Full Name** | `Jim Lee` | Komoot profile & GitHub README |
| **Exposed Email** | `jimleepro1@gmail.com` | Git commit patch extraction (`.patch`) |
| **Phone Number** | `+40 743 321 239` | Active OSINT / Email auto-responder correlation |
| **City** | `Timișoara` (Romania) | Registered business footprint & geo-indexing |
| **Tram Station** | `Piața Gheorghe Domășneanu` | Historical location trace (May 7, 2026) |

---

## Key Takeaways

1. **Git Metadata Leaks:** Developers often forget that `git commit` embeds the author's local email configuration into raw commit headers regardless of GitHub profile privacy settings.
2. **Speed & Efficiency:** Advanced search operators (Google Dorking) drastically reduce investigation overhead when correlating exposed indicators of compromise (IoCs) or PII.
3. **Passive vs. Active OSINT:** Combining passive footprinting (social platform inspection) with active interaction pathways yields rapid verification of target identity.
