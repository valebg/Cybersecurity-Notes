# 🔍 OSINT & Image Forensics Cheatsheet

Quick reference guide for media investigation, metadata analysis, and social media tracking in CTF challenges and IR triage.

---

## 📌 Methodology Flowchart

1. **Visual Reconnaissance:** Inspect embedded text, badges, dates, location markers, and character/concierge names.
2. **Metadata Examination:** Extract EXIF properties (creation dates, software, comments, GPS).
3. **Embedded Data Analysis:** Inspect binary strings, LSB layers (PNG), and file signatures.
4. **Social Engineering / OSINT:** Track target entities across social platforms (Instagram, Twitter/X, LinkedIn).
5. **Payload Decoding:** Process identified encoded buffers (Base64, Hex, ROT).

---

## 🛠️ Essential CLI Toolkit

### 1. Metadata Extraction (EXIF)
Extracts detailed file properties, edit history, software fingerprints, and embedded comments.
```bash
exiftool sample_image.png

2. Binary String Extraction
Searches for human-readable strings and pattern matches (flags, URLs, credentials, usernames).

Bash
strings sample_image.png | grep -iE "THM{|flag|http|instagram|user|secret"
3. File Signature & Container Analysis
Scans files for embedded archives (ZIP, TAR, RAR) or appended data streams.

Bash
# Scan for embedded files
binwalk sample_image.png

# Extract identified payload streams
binwalk -e sample_image.png
4. LSB Analysis for PNG Images
Analyzes Least Significant Bit (LSB) steganography in PNG images.

Bash
zsteg -a sample_image.png | grep -iE "http|instagram|THM|flag|user"
5. In-line Base64 Decoding
Decodes Base64 payloads directly in the terminal interface.

Bash
echo "ENCODED_STRING_HERE" | base64 -d
💡 Social Media OSINT Workflow
Entity Identification: Locate primary brand or organizational profiles.

Network Mapping: Inspect the Following list of primary accounts to locate linked secondary personas (e.g., concierge, admins).

Content Triage: Review post captions, photo metadata, and comments for encoded payloads.
