# HP-MDC - Hybrid Pattern Malware Detection and Categorization
HP-MDC is an Android Malware Detection (one of the classic pattern recognition issues) framework. It combines malware’s patterns from network traffic and code graph structure.

For the network traffic feature based module, we split the raw PCAP file to the network flow (groups network packet with a 5-tuple, the network flow should have the same (sourceID, sourcePort, destinationIP, destinationPort, Protocol)). And then we convert each network packet to a 784-byte gray image.  In our case, we refer to the Android Adware and General Malware Dataset (CIC-AAGM2017) https://www.unb.ca/cic/datasets/android-adware.html. 
We created and released our dataset AndroNetMnist, which includes 3,255,391 2D gray images in five classes for network traﬀic classification. Please check out it with this link https://drive.google.com/drive/folders/1XkVuy2BuvbMKabELEUpBZ1sGK1iQWBmW?usp=sharing. 



For the program code feature based module, we introduce natural language processing inspired methods in our malware detection and categorization framework.
