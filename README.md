# restart


# Week 1

## Day 1
* Administration
* Details about the Internet / architecture
* Who are you?
* What is the cloud?
* Cloud vs On-Premises (On-Prem) and Hybrid
* Service Types: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS)
* Operating System overview
* Version Control Basics & GitHub
* Using Discord
* Installing Python & Visual Studio Code

## Day 2
* Hardware & Brief history of computers
* CPU (Cores/Threads)
* RAM / Memory
* GPU (lots of cores)
* SSD/HDD
* Choosing components when building or deploying a server
* Cloud Pricing: [AWS Pricing Calculator](https://calculator.aws)

## Day 3
* Operating Systems: History, UNIX family: Linux, BSD, MacOS, Android, iOS, Windows
* Virtualization, Virtual Machines, and AMIs (Amazon Machine Images)
* Databases: Relational (SQL) and Non-relational (NoSQL)
* Shared Responsibility Model Basics
* Object Storage (S3 / Simple Storage Service)
* x86 vs ARM (in light details)
* `ping`, `traceroute` / `tracert`
* EC2 Lab - Deploying a virtual machine

## Day 4
* Networking Basics (IPv4)
* Ports Basics
* HTTP & Request/Response basics
* Firewalls (The concept)
* Python interpreter & HTTP module
* EC2 Lab Continued - Connecting to it



# Week 2 Topics

## Day 1
* Virtualbox & Virtual Machines
* Linux Kernel Overview
* [Shells](https://en.wikipedia.org/wiki/Unix_shell)
* [Directory Structure](https://linuxhandbook.com/linux-directory-structure/)
* Basic Commands: `man`, `ls`, `cd`, `pwd`, `mkdir`
* Using `sudo`
* Package Management (yum, apt, and others)


## Day 2
* More Basic Commands: `touch`, `cat`, `more`, `less`, `head`, `tail`, `cp`, `rm`, `mv`, `rmdir`, `find`
* Piping data with `|`
* Creating files (file redirection) with `>`
* Text Editors: `vim` basics, `nano`, and mention of gedit/visual studio code
* Understanding output of `--help` and arguments from manpages.
* Contents of /sbin directory
* Symbolic Links
* [CommandLineFu.com](https://www.commandlinefu.com/commands/browse/sort-by-votes)


## Day 3
* Working with `jobs`: Ctrl-Z (suspend), `fg`, `bg`, `jobs`
* Working with users/groups
* Understanding `/etc/passwd`
* [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) - /bin, /boot, /dev, etc.


## Day 4
* File Permission basics with `chmod` and `chown`.
* Understanding the output of `ls -al`
* Managing Processes with `ps`, `top`, `htop`, `grep`, `kill`
* Signals (`man signal`)
* Systemd and services with `systemctl`.
* Networking basics with `ip` (and the older/deprecated `ifconfig`)
* Log files and `/var`.
* [Modern Unix Replacements](https://github.com/ibraheemdev/modern-unix)

# Week 3

## Day 1

### Core Topics
* Basics of using Bash
* Setting the PATH environment variable and how it works.
* Creating/removing aliases in Bash with the `alias` and `unalias` commands.
* Listing environment variables with `env` and setting them with `export`.
* Using `which` to get location of a commands.
* `echo`, 
* Accessing a variable e.g. `echo $HOME`
* Installing `git` & `fzf`
* Running scripts from `./`
* Making a file *executable* with `chmod +x`

### Supplementary Topics
* [Awesome Cheatsheets - Bash Cheat Sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
* [GitHub Topics - Bash](https://github.com/topics/bash)
* [Valve rm -rf bug](https://www.theregister.com/2015/01/17/scary_code_of_the_week_steam_cleans_linux_pcs/)


## Day 2

### Core Topics
* Reading and writing Bash/shell scripts.
* Running commands with `$( )` e.g. `$(whoami)`.
* File permissions with chmod using symbolic (u+x, g-rw, o+rwx, ug-x, etc.) or octal (700, 444, 111, etc.) notation.
* Conditionals with `if`, `elif`, and `else`.
* Persisting aliases and changes to `PATH` by editing `.bashrc`.
* Using `curl`.

### Supplementary Topics
* [DevHints.io Bash Cheat Sheet](https://devhints.io/bash)
* [Cheat.sh - Cheat Sheets](https://cht.sh/)
* [tldr - Better documentation for  commonly used apps](https://github.com/tldr-pages/tldr)
* [The Art of Command Line - Master the Basics section](https://github.com/jlevy/the-art-of-command-line)


## Day 3

### Core Topics

* Base-10 (Decimal) Revision, Base-8 (Octal), Base-16 (Hexadecimal/Hex), and Base-2 (Binary)
* Know how to count to 16 in binary and hex.
* Converting between bases
* ASCII
* Networking Concepts: Modems, Routers, Switches
* Internet Protocol (IPv4 & IPv6)
* TCP & UDP (Connection vs Connectionless)
* Ports
* IP Subnetting Basics (History & Classful Addressing)
* Signed vs Unsigned numbers
* Integer Overflows (and the Gangnam Style viewcount bug)

* Example of integer overflow (just for demonstration purposes, you don't need to know C for the course)
```c
#include <stdio.h>
#include <unistd.h>

int main() {  // Press Ctrl-C to exit if it gets stuck looping forever.
  //int counter = 0;  // Example of how the counter should work without an overflow.
  //unsigned char counter = 0; // 8-bit. Resets to 0 when it overflows above 256.
  char counter = 0;  // 8-bit. Overflows to -128 when it overflows.

  for (counter = 0; counter <= 300; counter++) {
    printf("Value: %d\n", counter);

    // Sleep for 50 milliseconds.
    usleep(50 * 1000);
  }
}
```

### Supplementary Topics
* Software Bugs: Y2K, Knight Capital, 787 Dreamliner overflow, 737 MAX, Mars Orbiter, 2038 Bug (Epochalypse)
* What packets look like in `tcpdump`.
* What files look like in a hex viewer (such as `xxd` or [hexyl](https://github.com/sharkdp/hexyl))
* Basics of how a disassembler works.



## Day 4

### Core Topics
*  Line Endings (LF aka 0x0a on Linux/MacOS, vs CRLF aka 0x0d0a on Windows)

```
00000000: 7468 6973 2069 730a 610a 7465 7374 0a74  this is.a.test.t
00000010: 6f0a 7365 650a 6966 0a6c 696e 6566 6565  o.see.if.linefee
00000020: 6473 0a61 7265 0a73 7469 6c6c 0a62 7567  ds.are.still.bug
00000030: 6765 640a 696e 0a6e 6f74 6570 6164 0a    ged.in.notepad.

vs

00000000: 7468 6973 0d0a 6973 0d0a 616e 6f74 6865  this..is..anothe
00000010: 720d 0a74 6573 740d 0a6f 660d 0a6e 6577  r..test..of..new
00000020: 6c69 6e65 0d0a 6368 6172 6163 7465 7273  line..characters
```

* DHCP vs Static IPs (Basics)
* [Public vs Private IP Addresses - Private Network](https://en.wikipedia.org/wiki/Private_network)
* [Network Address](https://en.wikipedia.org/wiki/Network_address)
* [Default Gateway](https://en.wikipedia.org/wiki/Default_gateway)
* [Broadcast Address](https://en.wikipedia.org/wiki/Broadcast_address)
* Classless Inter-Domain Routing (CIDR) (/14, /24 etc)
* Regional Internet Registries (RIRs, ARIN, RIPE, APNIC, AFRINIC, LACNIC)
* [Internet Assigned Numbers Authority (IANA)](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority)
* Interpreting data from `whois`.
* [Country-Code Top-Level Domains (ccTLDs)](https://en.wikipedia.org/wiki/Country_code_top-level_domain)
* OSI Model & TCP Model Basics
* DNS Basics (A-record, converts domain name to IP address)

### Supplementary Topics
* [Computerphile - Unicode/UTF-8](https://www.youtube.com/watch?v=MijmeoH9LT4)
* [ipcalc](http://jodies.de/ipcalc)
* [CountryIPBlocks - Create an Access Control List - Select CIDR](https://www.countryipblocks.net/acl.php)
* [ANSI Escape Codes for colors in terminals](https://en.wikipedia.org/wiki/ANSI_escape_code)


# Week 4

## Day 1

### Core Topics
* Revision
* More CIDR & Subnetting
* VPC Basics


### Supplementary Topics
* [IPv4, CIDR, and VPC Subnets Made Simple - Ryan Schachte](https://www.youtube.com/watch?v=z07HTSzzp3o)
* [Classless Inter-Domain Routing - Professor Messer](https://www.youtube.com/watch?v=rJXvFWY4Ak0)
* [Subnetting Game - Practice Mode](https://www.subnetting.net/Subnetting.aspx?mode=practice)


## Day 2

### Core Topics
* Boolean Algebra Basics (AND, OR, and NOT)
* More Networking & Subnetting
* An IP address is just a 32-bit integer. e.g. http://2899908654/ and http://0xacd9182e/
* Using `netstat` to show active connections.
* Security - Network Discovery (nmap)
* Router settings: DHCP, Subnets, Route Tables, NAT (Network Address Translation) & Ports


### Supplementary Topics
* None, just practice the labs on Canvas.


## Day 3

### Core Topics
* Cyber Kill Chain (Overview)
* Vulnerabilities
* Risk & Security Trade-offs
* Responsible Disclosure
* Bug Bounties & HackerOne
* Zero-days / 0days.
* APT Groups
* White, grey, and black hats.
* Red (Offense) & Blue (Defense) Teams
* Social Engineering Attacks
* VPC Subnetting Lab


### Supplementary Topics
* [ProcessExplorer - Understanding Functionality](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)
* [Zoom 0day w/ $200k bounty. RCE (remote code execution)](https://blog.malwarebytes.com/exploits-and-vulnerabilities/2021/04/zoom-zero-day-discovery-makes-calls-safer-hackers-200000-richer/)
* [PrintNightmare](https://us-cert.cisa.gov/ncas/current-activity/2021/06/30/printnightmare-critical-windows-print-spooler-vulnerability)
* [Social Engineering Passwords](https://www.youtube.com/watch?v=opRMrEfAIiI)


## Day 4

### Core Topics
* CIA Triad - Confidentiality, Integrity, Availability
* Encryption Basics. Classical ciphers (rot13/Caesar cipher), brief mention of AES.
* At-rest vs In-transit
* Hashing
* Password Managers (BitWarden, LastPass, KeePass, etc)
* Storing Passwords: Salting & Pepper. Why MD5 is bad, why bcrypt, scrypt, and Argon2 are good.
* Identifying Fraudulent Emails - [FBI's mailserver hacked a few days prior](https://www.reddit.com/r/sysadmin/comments/qsun7o/email_from_fbi_looks_odd/) 
* MD5 and its problems (fast & collisions)


### Supplementary Topics
* [Create your own MD5 collisions - plane.jpg and ship.jpg](https://natmchugh.blogspot.com/2015/02/create-your-own-md5-collisions.html))
* [HaveIBeenPwned](https://haveibeenpwned.com/)


# Week 5

## Day 1

### Core Topics
* TryHackMe
* Bruteforcing: icloud & instagram bugs
* Estimation of time required to bruteforce all 10-char passwords
* Analysis of an attack. Spammer using an open mailing form to send spam. Analyzing webserver logs to identify spammer.
* Question about people who fall for scam apps. Techniques to identify scams.
* [CVE](https://cve.mitre.org/cve/search_cve_list.html)
* [ATT&CK](https://attack.mitre.org/) & [D3FEND](https://d3fend.mitre.org/)
* [SecLists on GitHub - Leaked Passwords](https://github.com/danielmiessler/SecLists/)
* Encoding / Decoding
* How to create a hash of something in Python using `hashlib`

## Day 2

### Core Topics
* Python - Writing a small password strength checking program
* Control Flow (if/elif/else)
* Functions
* Modules


### Supplementary Topics
* [StackOverflow Developer Survey & Choosing Technology for your Career](https://insights.stackoverflow.com/survey/2021)
* [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar)


## Day 3

### Core Topics

* More Python
* Containers: Lists, Tuples, Dictionaries
* Javascript/Node Basics: Variables/Lists (arrays) and surface similarity with Python
* How minifying code saves bandwidth.
* Debugging
* Files (`open` and `close`)

### Supplementary Topics

* [Python Cheat Sheet - Basics, Flow Control, Functions, Lists](https://www.pythoncheatsheet.org)


## Day 4

### Core Topics
* More Python
* Loops (`for` & `while`)
* `time.sleep(10)`
* `random` library
* `string` library
* Python Conventions / Style Guide (PEP8)
* Linting




# Week 6

## Day 1

### Core Topics
* More Python
* Software Licenses
* Markdown
* Forking & Other GitHub features
* `with` keyword in Python (Known as *context managers*) for opening/closing resources.
* `socket` library basics and how network services communicate
* File Descriptors and the `/proc/<process_id>/fd` directory.


## Day 2

### Core Topics
* More Python
* `/etc/hosts` and `/etc/resolv.conf`
* `os` module and dangers of using `os.system(...)`
* Virtual Environments (`venv` module)
* JSON basics
* Exception Basics - Creating and raising a custom exception
* `netstat` Basics

### Supplementary Topics
* [Python Module Of The Week - PyMOTW](https://pymotw.com/3/)


## Day 3

### Core Topics
* More Python & how network services work
* More JSON
* Using [FastAPI](https://fastapi.tiangolo.com/) to create an API
* DevOps

### Supplementary Topics
* [HackerNews](https://news.ycombinator.com)
* [GitHub Student Developer Pack](https://education.github.com/pack) - Link GitHub with your @myunitec.ac.nz email address.
* [roadmap.sh](https://roadmap.sh)


## Day 4

### Core Topics
* Concurrency/threading basics
* Compiling basics (download, unzip, ./configure, make, run) - Compiled Python & redis
* Software Testing basics with `pytest`. Brief example of test driven development
* Database Basics (NoSQL)
* Basics of using [redis](https://redis.io)


### Supplementary Topics
* [Try redis](https://try.redis.io)


# Week 7

## Day 1

### Core Topics
* SQL Basics
* Data Manipulation Language (DML): `SELECT`, `FROM`, `WHERE`, `ORDER BY`, Comments
* `INNER JOIN` basics
* Date ranges with `BETWEEN`

### Supplementary Topics
* [StackShare.io](https://stackshare.io/)


## Day 2

### Core Topics
* Using SQL with [SQLite](https://sqlite.org/famous.html) (Vocareum labs were down)
* [SQLite Browser](https://sqlitebrowser.org/)
* [Sakila Database File - SQLite version](https://github.com/krp/sakila-sqlite) - Download the `sakila.db` file.
* Making queries with Python's `sqlite3` module
* Creating an API that talks to a database with FastAPI.


### Supplementary Topics
* None today. See `main.py` in this repo.


## Day 3
### Core Topics
* Entity-Relationship Diagrams
* Database Diagrams (and relationships)
* Database Normalization
* ACID
* SQL: `INSERT`
* Amazon RDS (Brief mention)
* Continued building API with `FastAPI` & `SQLite` with `sakila` database.

### Supplementary Topics
* [sqldbm.com](https://sqldbm.com)
* [dbdiagram.io](https://dbdiagram.io)


## Day 4
### Core Topics
* OOP Basics
* Amazon RDS
* MariaDB & PostgreSQL
* Finishing up API server (deploy to EC2)
* Using `scp`.


### Supplementary Topics
* [Design Pattern Basics](https://refactoring.guru/design-patterns)


# Week 8
## Day 1
### Core Topics
* Assignment Review
* Bad Bugs that occurred over the break: [Y2K22](https://arstechnica.com/information-technology/2022/01/exchange-server-bug-gets-a-fix-after-ruining-admins-new-years-plans/), [Log4Shell](https://en.wikipedia.org/wiki/Log4Shell), [CVE-2021-39659 (Emergency Services Broken on Android devices)](https://arstechnica.com/gadgets/2022/01/google-fixes-nightmare-android-bug-that-stopped-user-from-calling-911/)
* Containers
* Docker (Basics)

### Supplementary Topics
* [LiveOverflow - Log4Shell](https://www.youtube.com/watch?v=w2F67LbEtnk)


## Day 2
### Core Topics
* Cloud Adoption Framework
* Fact Finding Group Exercise
* [Well Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### Supplementary Topics
* [Well Architected Labs](https://wellarchitectedlabs.com/) - NOTE: Requires AWS Account for most of them so use after the course.


## Day 3
### Core Topics
* Assignment Help
* Cloud Practitioner Exam Prep
* [Anki](https://apps.ankiweb.net/)
* Using IAM, S3 & AWS CLI Basics

### Supplementary Topics
* [awscli examples](https://github.com/aws/aws-cli/blob/develop/awscli/examples/)


## Day 4
### Core Topics
* ssh, scp, rsync & public key cryptography revision
* iptables basics
* More S3 & awscli
* HTTP GET/POST revision & [Insomnia REST](https://insomnia.rest/)

### Supplementary Topics
* [iptables Cheatsheet](https://www.andreafortuna.org/2019/05/08/iptables-a-simple-cheatsheet/)
* [System Design Primer](https://github.com/donnemartin/system-design-primer/)


# Week 9

## Day 1
### Core Topics
* PaaS Basics & ElasticBeanstalk
* More Docker
* Windows Registry
* [Proxy Servers](https://en.wikipedia.org/wiki/Proxy_server)
* Nginx & [Reverse Proxies](https://en.wikipedia.org/wiki/Reverse_proxy)

### Supplementary Topics
* [Burp Suite](https://portswigger.net/burp)
* [Dec 2021 WebServer Survey](https://news.netcraft.com/archives/2021/12/22/december-2021-web-server-survey.html)


## Day 2
### Core Topics
* DNS in depth
* Registrars, Root Servers, Hosting, Resolvers
* ccTLD, gTLDs, Internationalized Domain Names & issues with them
* `whois` & `dig` (again)
* Zone Files (basics)
* DNS Based Load Balancing (Round-Robin DNS)
* NS, A, AAAA, MX, CNAME, SOA, TXT, SPF, PTR records
* Load Balancer Types (Application, Network), more detail tomorrow

### Supplementary Topics
* [CloudFlare Learning - DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)


## Day 3
### Core Topics
* Understanding metrics for scaling
* Vertical vs Horizontal Scaling
* EC2 Instance Types
* DB Replicas & Sharding
* Route53


# Day 4
### Core Topics
* More Git
* Container Basics (ECS, ECR, Fargate)
* Lambda Basics


# Week 10
## Day 1
### Core Topics
* DNS debugging case study
* Load balancer & other AWS services pricing
* Popular/common DockerHub images
* More containers / Docker
* HTML/CSS Basics

### Supplementary Topics
* [DockerCheatSheet.com](https://dockercheatsheet.com/)


## Day 2
### Core Topics
* Amazon Aurora Basics
* [Docker Compose](https://docs.docker.com/compose/) & container management/orchestration
* `docker-compose.yml` file syntax (services, ports, images)
* Getting services/containers to talk to each other
* Using a cache


### Supplementary Topics
* [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)
* [Troy Hunt - How I Got Pwned by My Cloud Costs](https://www.troyhunt.com/how-i-got-pwned-by-my-cloud-costs/)
* [redis-py Basics](https://redis.readthedocs.io/en/stable/)


## Day 3
### Core Topics
* More Docker Compose
* ElastiCache
* Elastic Block Store (EBS) with EC2
* EC2 Instance Stores vs EBS
* Creating/Attaching
* Filesystem Basics, Mounting/Unmounting
* `lsblk`, `xxd /dev/xvdf | less`, `parted -l`, `mkdir /mnt/mydisk`, `mount /dev/xvdf /mnt/mydisk`, `df -h`, create files on disk, `umount /mnt/mydisk`


### Supplementary Topics
* [ElastiCache](https://aws.amazon.com/elasticache/)


## Day 4
### Core Topics
* Storage Types (SSD, Magnetic, Tape)
* [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) 
* More on Filesystem & Types
* Network File Storage (NFS) Basics & Elastic File System (EFS)
* Block Storage vs Object Storage
* More S3
* Glacier & Archival


## Supplementary Topics
* [AWS S3 CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html)
* [AWS Glacier via CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-glacier.html)
* [Fallacies of Distributed Computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)


# Week 11
## Public Holiday - No Class on 1st Day of Week

## Day 1
### Core Topics
* Group Exercise review of AWS products for Compute, Storage, Databases, Security, IoT, and Frontend/Web/Mobile
* Intro to CloudWatch
* Debugging & benefits of logging (example with 2degrees topups & payment providers)
* CloudTrail basics

## Day 2
### Core Topics
* Gathering metrics w/ CloudWatch (CPU, Memory, Storage usage)
* Security Groups & Firewall revision
* Web-server logs & deeper dive into network traffic with [Wireshark](https://www.wireshark.org/) (basics)
* Monitoring Infrastructure Lab (CloudWatch)

### Supplementary Topics
* [Cloud Foundations Learning Plan](https://explore.skillbuilder.aws/learn/public/learning_plan/view/82/cloud-foundations-learning-plan)


## Day 3
### Core Topics
* EC2 Launch templates
* Infrastructure as Code: [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [Terraform](https://www.terraform.io/), [Pulumi](https://www.pulumi.com/)
* CloudTrail Lab & Log Management/Analysis

### Supplementary Topics
* [Cross Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
* Useful services used via APIs: [Twilio](https://www.twilio.com/), [Sendgrid](https://sendgrid.com/), [Auth0](https://auth0.com/), [Sentry](https://sentry.io/welcome/)


# Week 12
## Day 1 Waitangi Day - Again no class

## Days 2 & 3
### Core Topics
* Knowledge Checks
* Practice Preparation for Cloud Practitioner Exam

## Day 4
### Core Topics
* Student Live Demos of awscli & AWS services
* Test


## Day 5
### Core Topics
* Careers & Industry Event
* End of semester

### Supplementary Topics
* [PDF - Cloud Practitioner Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf)
* [AWS Skill Builder - Cloud Foundations Learning Plan](https://explore.skillbuilder.aws/learn/public/learning_plan/view/82/cloud-foundations-learning-plan)
