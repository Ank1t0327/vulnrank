# Vulnrank

##  Overview

**Vulnrank** is a lightweight reconnaissance and prioritization tool built for security researchers and bug bounty hunters. It automates subdomain enumeration, filters live targets, and assigns risk-based scores to help you focus on what actually matters.

Instead of drowning in hundreds of subdomains, Vulnrank highlights the ones most likely to be vulnerable.

---

##  Features

-  Subdomain Enumeration
-  Live Host Detection
-  Intelligent Filtering
-  Risk-Based Scoring System
-  Fast and Minimal Workflow

---

##  How It Works

1. Collects subdomains for a target domain  
2. Checks which hosts are alive  
3. Filters out noise (irrelevant/duplicate entries)  
4. Assigns a score based on exposure patterns  
5. Outputs prioritized targets  

---

##  Installation

```bash
git clone https://github.com/Ank1t0327/vulnrank.git
cd vulnrank
pip install -r requirements.txt
