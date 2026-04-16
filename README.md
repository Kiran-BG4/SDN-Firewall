 SDN-Based Firewall using POX Controller

# Project Description

This project implements a **Software Defined Networking (SDN) based firewall** using the POX controller and Mininet emulator. The firewall dynamically inspects network packets and applies filtering rules based on IP addresses and TCP port numbers.

---

# Objectives

* To understand SDN architecture and centralized control
* To implement a firewall using a POX controller
* To perform packet inspection and filtering
* To block/allow traffic based on defined policies

---

##  Key Concepts

* **SDN (Software Defined Networking):** Separates control plane and data plane
* **POX Controller:** Acts as the brain of the network
* **Mininet:** Simulates a network topology
* **OpenFlow:** Protocol used for communication between switch and controller

---

## ⚙️ Technologies Used

* Python
* POX Controller
* Mininet
* OpenFlow Protocol
* Ubuntu (Linux Environment)

---

# Features Implemented

*  IP-based filtering (blocks communication between specific hosts)
*  Port-based filtering (blocks HTTP traffic on port 80)
*  Selective traffic control (other traffic allowed)
*  Real-time packet inspection
*  Logging of blocked traffic in `firewall_log.txt`

---

# System Architecture

```
Host (h1, h2, h3)
        ↓
    OpenFlow Switch
        ↓
   POX Controller (Firewall Logic)
```

---

# Working Principle

1. Hosts send packets through the network
2. The switch forwards packets to the POX controller
3. The controller inspects packet details (IP, TCP port)
4. Based on rules:

   * Blocks unwanted traffic 
   * Allows valid traffic 
5. Blocked events are logged in a file


---

# How to Run the Project

### Step 1: Start POX Controller

```bash
sudo killall python3.9
sudo mn -c
cd ~/pox
python3.9 pox.py log.level --DEBUG openflow.of_01 firewall
```

---

### Step 2: Start Mininet (New Terminal)

```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3
```

---

### Step 3: Test Connectivity

```bash
pingall
```

---

### Step 4: Test HTTP Blocking

```bash
h1 wget http://10.0.0.2
```
# incase of the port is under use then 
```bash
sudo lsof -i :6633
sudo kill -9 <pid>
```
 -> we have used the 6633 port number so we are checking the process id using the port 6633 
 -> if the port is under use then we kill that process using that pid
---

# Expected Results

*  Communication between h1 and h2 is blocked
*  HTTP traffic (port 80) is blocked
*  Communication with other hosts is allowed
*  Logs are stored in `firewall_log.txt`



##  Conclusion

The project successfully demonstrates the implementation of a **centralized SDN-based firewall** capable of dynamically controlling network traffic using programmable rules.
It highlights the flexibility and efficiency of SDN in modern network security.

---

# Future Scope

* Add GUI for firewall management
* Implement dynamic rule configuration
* Detect network attacks (port scanning, DoS)
* Support multi-switch topologies


