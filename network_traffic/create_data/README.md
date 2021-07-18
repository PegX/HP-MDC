# Create AndroNetMnist dataset

To create the ANdroNetMnist we use the CIC-AAGM2017 (Android Adware and General Malware Dataset) dataset, which can be found with https://www.unb.ca/cic/datasets/android-adware.html. In our case, we just consider the network traffic dataset from CIC-AAGM2017. After we get the dataset, we split each network package (PCAP) file to multiple network flows and map each network flow to a 2D-grap image. The method is similar with USTC-TK2016 https://github.com/yungshenglu/USTC-TK2016.

We use the code of the first two steps in USTC-TK2016 works, which can be found with 
https://github.com/yungshenglu/USTC-TK2016#execution

We describe the methods as follows:

## Methods
### Dependencies
numpy
PIL

### Experiment setup
1. Linux 3.18-lp152.60-default x86_64 x86_64 x86_64 GNU/Linux
2. Mono
3. Python3


### Steps
#### Prepar the original PCAP dataset
we get the CIC-AAGM2017 (Android Adware and General Malware Dataset) dataset, which can be found with https://www.unb.ca/cic/datasets/android-adware.html. This dataset includes five zipped files.
Adware-PCAPs.zip  Benign-PCAPs.zip  Ransomware-PCAPs.zip  Scareware-PCAPs.zip  SMSmalware-PCAPs.zip
Please unzip them and put them under 1_Pcap folder.

#### Split the PCAP file by each flow.
#####
Following the USTC-TK2016 guideline, we split the pcap files by running the powershell script. 

PS> .\1_Pcap2Session.ps1

If succeed, there are two new created folders in folder 2_Session\
- AllLayers
- L7
We choose AllLayers as our target and continue the following steps.

#####
After getting the splitted flows, we run the ProcessSession script to process the splitted flow and generate PCAP files, which only have one network flow in each PCAP file.

PS> .\2_ProcessSession.ps1

If succeed, you will see the FilteredSession\ and TrimedSession\ folders under 3_ProcessedSession\. The files under FilteredSession are original network flows from PCAP files and trimmed PCAP files with the size of 784 bytes.

#####
After geting the TrimedSession files, we use findout.py script to prepare our dataset for binary classification(Malware Detection) and multi-classification(Malware categorization)

python3 findout.py

If successed, there are two new folders: TrimedSession_2 and TrimedSession_5 will be created.
1. TrimedSession_2 stores the files for binary classification (malware detection)
2. TrimedSession_5 stores the files for mutli-classification (malware categorization)

After preparing the files for binary classification and multi-classifcation. We use script to convert the 784 network flow to binary PNG files by running:
1. python3 3_Session2Png_binary.py
2. Python3 3_Session2Png_multi.py

#####
The last but not least step for preparing the ANdroNetMnist dataset is collected all converted PNG to Mnist-alike dataset.
In our work, we give the malware detection dataset. For the malware categorization, this step is similar. The only difference is the different script to run.
python3 4_Png2Mnist.py

