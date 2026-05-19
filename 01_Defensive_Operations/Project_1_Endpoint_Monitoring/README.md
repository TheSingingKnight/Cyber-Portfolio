# Project 1: Windows Endpoint Monitoring & SIEM Ingestion

## Project Origins
This lab wasn't built in a vacuum; it was designed as the defensive foundation for a unified "Cyber Range" mission. My goal was to create a sandbox where I could bridge the gap between theoretical security and the actual friction of engineering a data pipeline.

To demonstrate a full security lifecycle, I am stringing together three distinct projects:
* **Defensive Operations:** This current report on building endpoint visibility.
* **Vulnerability Management:** Probing the environment for weaknesses using Nessus.
* **Adversarial Lifecycle:** Simulating an attack to see if my defensive configurations actually catch the threat.

---

## 1. The Mission Objective
The primary goal was to establish total visibility over a Windows 10 endpoint. I aimed to move beyond basic event logging to capture high-fidelity telemetry that could later be used to detect the adversarial simulations I plan to run later in this series.

> **Analyst’s Note:** I prioritised this project first because you cannot defend what you cannot see. Establishing this "Defensive Hub" was a functional requirement before I could move on to scanning or attacking the environment.

---

## 2. Technical Foundations: Why I chose this stack
* **Splunk Enterprise:** I chose Splunk as the central "Brain" of the lab. Its ability to handle diverse data types makes it the ideal hub for a growing lab ecosystem.
* **Sysmon (System Monitor):** Standard Windows logs often miss the "how" of an attack. I installed Sysmon to get kernel-level detail, such as process command lines and network connections, which are vital for forensic analysis.
* **Splunk Universal Forwarder (UF):** To keep the target machine performant, I used the UF to securely ship logs over port `9997`.

---

## 3. Lab Environment: Building the Sandbox
Following a "Security by Design" approach, I built a segmented environment to protect my host system and simulate a real-world network.

* **Defensive Hub:** Windows 10 (Serving as the target endpoint, hosting Sysmon for high-fidelity telemetry and the Splunk Universal Forwarder for secure data transmission). 
* **SIEM & Offensive Hub:** Kali Linux (Acting as the attacker’s vantage point while simultaneously serving as the central "Brain" of the lab by hosting the Splunk Enterprise instance). 
* **Legacy Target:** Metasploitable 2 (An intentionally vulnerable environment designed to provide a target-rich testing ground for security probing and exploitation).

| Asset Name (VirtualBox) | Hostname | IP Address | Role |
| :--- | :--- | :--- | :--- |
| **Kali-Offensive-Hub** | `kali` | `192.168.56.102` | Attacker / SIEM Hub |
| **Win10-Defensive-Hub** | `Win10-Defensive` | `192.168.56.106` | Windows Defensive Hub |
| **Metasploitable2-Legacy-Target** | `metasploitable` | `192.168.56.104` | Legacy Linux Target |

---

## 4. Technical Evidence (The Showcase)

### [Screenshot 1 - The Cyber Range]
A view of the VirtualBox Manager showing the segmented lab architecture.

![The Cyber Range](images/P1_R1_Cyber_Range.png)

### [Screenshot 2 - Connectivity Proof]
A Splunk search result confirming the Win10-Defensive host is successfully shipping real-time telemetry.

![Connectivity Proof](images/P1_R2_Connectivity_Proof.png)

### [Screenshot 3 - Granular Ingestion]
A high-fidelity search proving Sysmon is successfully capturing kernel-level activity.

![Granular Ingestion](images/P1_R3_Granular_Ingestion.png)

### [Screenshot 4 - The "Whoami" Capture]
Result of `EventCode=1` (Process Creation) showing the system tracking a specific analyst command.

![The Whoami Capture](images/P1_R4_Whoami_Capture.png)

### [Screenshot 5 - Tactical Visualization]
A bar chart generated to demonstrate the ability to transform raw logs into security intelligence.

![Tactical Visualization](images/P1_R5_Tactical_Visualization.png)

---

## 5. Strategic Analysis: The Value of Visibility
In a professional setting, data is noise until it is refined into intelligence. By configuring Sysmon to capture specific Event IDs, I’ve created a "Digital Tripwire." This setup is relevant because it demonstrates the shift from reactive logging to proactive monitoring.

Without this foundation, an analyst is essentially blind to lateral movement or "Living off the Land" techniques. This project proves I can build the eyes of an organisation before we ever try to defend its heart.

---

## 6. Defensive Maturity & Hardening Roadmap
While the environment is functional, it is currently in a "Passive" state. To reach production-grade maturity, I would implement the following "how-to" steps:

* **Configuration Tuning:** I would deploy a curated XML configuration (such as SwiftOnSecurity’s) to filter out common background noise and focus purely on high-risk directories.
* **Real-Time Alerting:** Building triggers for "Living off the Land" binaries like PowerShell, I would use Splunk’s Search Processing Language (SPL) to create automated triggers for `EventCode=1` (Process Creation) when system tools like `vssadmin` or `powershell` are invoked unexpectedly.
* **Tactical Dashboards:** I would leverage Splunk Dashboard Studio to aggregate raw telemetry into visual trends, allowing for a 24/7 "at-a-glance" security posture.

---

## Key Skills Demonstrated
* SIEM Engineering (Splunk)
* Endpoint Detection & Response (Sysmon)
* Security by Design (Lab Segmentation)

