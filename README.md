# tcp_stat
Simple TCP/IP socket pinger.

**Usage:**
```
python tcpstat.py [HOST] [PORT]
```

**Example:**
```
$python tcpstat.py google.com 80
Validating port: 80...
Validating port (80) for 1 time(s)...
Port (80) seems to be valid.
Initializing TCP ping on 172.217.31.14:80...

Host Status:
✔ Online: 122.94 ms
✔ Online: 122.19 ms
✔ Online: 87.16 ms
✔ Online: 82.76 ms
```
