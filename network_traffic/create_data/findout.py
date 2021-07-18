import os
prefix_1 = 'TrimedSession'
prefix_1_1 = prefix_1 +'/Train/'
prefix_1_2 = prefix_1 +'/Test/'
prefix_2 = 'TrimedSession_5'
prefix_2_1 = prefix_2 +'/Train/'
prefix_2_2 = prefix_2 +'/Test/'
#ad-ALL  be-ALL  ra-ALL  sc-ALL  sms-ALL
paths = ['ad-ALL/','be-ALL/','sc-ALL/','sms-ALL/','ra-ALL/']
print("Preparing training dataset for five categorization")
for path in paths:
    count = 0
    for root,path_,files in os.walk(prefix_1_1+str(path)):
        for file_ in files:
            if file_.endswith('.pcap'):
                _file_ = os.path.join(root,file_)
                count += 1
                os.system("cp " + _file_ +" " + prefix_2_1+str(path)+'/'+file_)
    print("path :",path,count)
    #rm `ls -alh|grep '^d'` -rf
print("Preparing testing dataset for five categorization")
for path in paths:
    count = 0
    for root,path_,files in os.walk(prefix_1_2+str(path)):
        for file_ in files:
            if file_.endswith('.pcap'):
                _file_ = os.path.join(root,file_)
                os.system("cp " + _file_ +" " + prefix_2_2+str(path)+'/'+file_)
    print("path :",path,count)
prefix_3 = 'TrimedSession_2'
prefix_3_1 = prefix_3 + '/Train/'
prefix_3_2 = prefix_3 + '/Test/'
target_paths = ['be-ALL/','ma-ALL/']
print("Preparing training dataset for binary classification")
countM = 0
countB = 0
for path in paths:
    for root,path_,files in os.walk(prefix_1_1+str(path)):
        for file_ in files:
            if file_.endswith('.pcap'):
                if '-be-' in file_:
                    countB+=1
                    _file_ = os.path.join(root,file_)
                    os.system("cp " + _file_ +" " + prefix_3_1+str(target_paths[0])+'/'+file_)
                elif ('-ad-' in file_) or ('-sc-' in file_) or ('-sms-' in file_) or ('-ra-' in file_):
                    countM+=1
                    _file_ = os.path.join(root,file_)
                    os.system("cp " + _file_ +" " + prefix_3_1+str(target_paths[1])+'/'+file_)
print("Training Malware :",countM, "Benign",countB)

countM = 0
countB = 0
print("Preparing testing dataset for binary classification")
for path in paths:
    for root,path_,files in os.walk(prefix_1_2+str(path)):
        for file_ in files:
            if file_.endswith('.pcap'):
                if '-be-' in file_:
                    countB += 1
                    _file_ = os.path.join(root,file_)
                    os.system("cp " + _file_ +" " + prefix_3_2+str(target_paths[0])+'/'+file_)
                elif ('-ad-' in file_) or ('-sc-' in file_) or ('-sms-' in file_) or ('-ra-' in file_):
                    countM += 1
                    _file_ = os.path.join(root,file_)
                    os.system("cp " + _file_ +" " + prefix_3_2+str(target_paths[1])+'/'+file_)

print("Training Malware :",countM, "Benign",countB)
