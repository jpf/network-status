Goal: Tell at a glance what my connectivity is, and why it's that way
Questions answered:
- Am I connected to the internet?
- What is my average ping time?
- Is my average ping time good?
- Is my average ping time increasing, decreasing, or mostly stable?
- What is my packetloss?
- Is my packetloss acceptable?
- Is my rate of packetloss increasing, decreasing, or mostly stable?
- What interface am I connected to the internet through? (en1, en0, etc)
- What is the name of that interface? (Wired Ethernet, Wi-Fi, etc)
- What are the historical statistics for networks I connect to SSID?
- Is DNS resolving?
- Is DNS being hijacked?
- Can I fetch publically accessable websites?

Order:
  What interfaces do I have?
  Which of them are active?
* Which active interface(s) is our default route?
* What is the IP address on the default route interface?
* What is the gateway of the default route?
* Can I ping that gateway?
* What is the gateway's avg ping time?
* What is the gateway's packetloss rate?
* Can I ping past the gateway?
* What is the avg ping time of the remote host?
* What is the packetloss to the remote host?
  Do we have default DNS servers?
* Are they resolving DNS?
* Are they resolving DNS _correctly_?
* Can we make HTTP requests to public HTTP servers?
* Can we SSH to any of our SSH servers?

en0 (Wi-Fi) - gw:192.168.1.1 - extip:76.120.66.180 (6.21ms/4.5%) - ping: (70.14ms / 1.62%)

if   name    ip            gateway     gwp gwl   |  ping      loss   dns http SSH  remote ip      
en0  Wi-Fi  ↻192.168.1.10  192.168.1.1 9ms 4.24% | ↗240.23ms ↓4.50%  Y   Y    Y    76.120.66.180  

if  ip gw gp  gl  | p     l   D H S
en0 *  *  9ms 4%  | 240ms 5%  * * *




↑32.21ms 
↗25.21ms
 20.21ms
↘15.21ms
↓10.42ms


interface: en0 (Wi-Fi) 
gateway:  192.168.1.1 (4.21 ms / 2.14%)
external: 76.120.66.180
dns: OK



$ networksetup -listallhardwareports
