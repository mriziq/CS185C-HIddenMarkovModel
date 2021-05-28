import os
import operator
import random

def counter(lst, x):        # Helper function to return element count
    return lst.count(x)

def splitDataList(list_malware, percent):                   # Helper function to partition datasets
    howManyNumbers = int(round(percent*len(list_malware)))
    shuffled = list_malware[:]
    random.shuffle(shuffled)
    return shuffled[howManyNumbers:], shuffled[:howManyNumbers]


####### WINWEBSEC #######
path = "Malicia-Big3-Opcodes/winwebsec/"
filelist = os.listdir(path)
for x in filelist:
    with open(path + x, "r") as y:
        read_data_winwebsec = y.read()

unique_winwebsec = []
dist_winwebsec = {}
unique_count_winwebsec = 0
ranked_dist_winwebsec = {}
ranked_dist_winwebsec["A"] = []
ranked_dist_winwebsec["B"] = []
ranked_dist_winwebsec["C"] = []

list_winwebsec = read_data_winwebsec.split()

for item in list_winwebsec:
    if item not in unique_winwebsec:
        unique_count_winwebsec += 1
        unique_winwebsec.append(item)   

for unique in unique_winwebsec:
    x = counter(list_winwebsec, unique)
    dist_winwebsec[unique]= x 

sorted_dist_winwebsec = dict(sorted(dist_winwebsec.items(), key=operator.itemgetter(1), reverse=True)) 

for key in sorted_dist_winwebsec:
   
    if sorted_dist_winwebsec[key] >= 100:
        ranked_dist_winwebsec["A"].append(key)

    if 10 <= sorted_dist_winwebsec[key] <= 99:
        ranked_dist_winwebsec["B"].append(key)

    if sorted_dist_winwebsec[key] <= 9:
        ranked_dist_winwebsec["C"].append(key)

for item in list_winwebsec:
    if item in ranked_dist_winwebsec["A"]:
        list_winwebsec[list_winwebsec.index(item)] = 0

    if item in ranked_dist_winwebsec["B"]:
        list_winwebsec[list_winwebsec.index(item)] = 1

    if item in ranked_dist_winwebsec["C"]:
        list_winwebsec[list_winwebsec.index(item)] = 2

trainingset_winwebsec = open("training-data/trainingset_winwebsec.txt", "w")
for element in list_winwebsec:
    trainingset_winwebsec.write(f'{element} \n')

trainingset_winwebsec.close()

####### ZBOT #######
path = "Malicia-Big3-Opcodes/zbot/"
filelist = os.listdir(path)
for x in filelist:
    with open(path + x, "r") as y:
        read_data_zbot = y.read()

unique_zbot = []
dist_zbot = {}
unique_count_zbot = 0
ranked_dist_zbot = {}
ranked_dist_zbot["A"] = []
ranked_dist_zbot["B"] = []
ranked_dist_zbot["C"] = []

list_zbot = read_data_zbot.split()

for item in list_zbot:
    if item not in unique_zbot:
        unique_count_zbot += 1
        unique_zbot.append(item)   

for unique in unique_zbot:
    x = counter(list_zbot, unique)
    dist_zbot[unique]= x 

sorted_dist_zbot = dict(sorted(dist_zbot.items(), key=operator.itemgetter(1), reverse=True)) 

for key in sorted_dist_zbot:
   
    if sorted_dist_zbot[key] >= 100:
        ranked_dist_zbot["A"].append(key)

    if 10 <= sorted_dist_zbot[key] <= 99:
        ranked_dist_zbot["B"].append(key)

    if sorted_dist_zbot[key] <= 9:
        ranked_dist_zbot["C"].append(key)

for item in list_zbot:
    if item in ranked_dist_zbot["A"]:
        list_zbot[list_zbot.index(item)] = 0

    if item in ranked_dist_zbot["B"]:
        list_zbot[list_zbot.index(item)] = 1

    if item in ranked_dist_zbot["C"]:
        list_zbot[list_zbot.index(item)] = 2

trainingset_zbot = open("training-data/trainingset_zbot.txt", "w")
for element in list_zbot:
    trainingset_zbot.write(f'{element} \n')

trainingset_zbot.close()

####### ZEROACCESS #######
path = "Malicia-Big3-Opcodes/zeroaccess/"
filelist = os.listdir(path)
for x in filelist:
    with open(path + x, "r") as y:
        read_data_zeroaccess = y.read()

unique_zeroaccess = []
dist_zeroaccess = {}
unique_count_zeroaccess = 0
ranked_dist_zeroaccess = {}
ranked_dist_zeroaccess["A"] = []
ranked_dist_zeroaccess["B"] = []
ranked_dist_zeroaccess["C"] = []

list_zeroaccess = read_data_zeroaccess.split()

for item in list_zeroaccess:
    if item not in unique_zeroaccess:
        unique_count_zeroaccess += 1
        unique_zeroaccess.append(item)   

for unique in unique_zeroaccess:
    x = counter(list_zeroaccess, unique)
    dist_zeroaccess[unique]= x 

sorted_dist_zeroaccess = dict(sorted(dist_zeroaccess.items(), key=operator.itemgetter(1), reverse=True)) 

for key in sorted_dist_zeroaccess:
   
    if sorted_dist_zeroaccess[key] >= 100:
        ranked_dist_zeroaccess["A"].append(key)

    if 10 <= sorted_dist_zeroaccess[key] <= 99:
        ranked_dist_zeroaccess["B"].append(key)

    if sorted_dist_zeroaccess[key] <= 9:
        ranked_dist_zeroaccess["C"].append(key)

for item in list_zeroaccess:
    if item in ranked_dist_zeroaccess["A"]:
        list_zeroaccess[list_zeroaccess.index(item)] = 0

    if item in ranked_dist_zeroaccess["B"]:
        list_zeroaccess[list_zeroaccess.index(item)] = 1

    if item in ranked_dist_zeroaccess["C"]:
        list_zeroaccess[list_zeroaccess.index(item)] = 2

trainingset_zeroaccess = open("training-data/trainingset_zeroaccess.txt", "w")

for element in list_zeroaccess:
    trainingset_zeroaccess.write(f'{element} \n')
trainingset_zeroaccess.close()
