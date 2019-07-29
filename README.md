# OSRS Ping Checker 

## Requirements

* Python 3

## Instructions

### 1. Clone repository 

### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Run script (NOTE: Must be run as root)

```
python pingcheckcli.py
```

## Sample output

```
[*] Retreiving worlds...
[+] Retreived worlds!
[*] Pinging World 301
[*] Pinging World 302
[*] Pinging World 303
[*] Pinging World 304
[*] Pinging World 305
....
[*] Pinging World 526
[*] Pinging World 527
[*] Pinging World 528
[*] Pinging World 529
[*] Pinging World 530
[+] Ping checks complete!
[+] The least amount of ping is world 527 with 15.41ms ping
[+] All results logged to text file: "results.txt"

```