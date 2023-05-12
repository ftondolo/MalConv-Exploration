import torch
import torch.nn as nn
import torch.nn.functional as F
import sys
import time
from collections import OrderedDict
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
import os
import time
import yaml
import numpy as np
import csv 
import pandas as pd
from google.colab import drive
from torch.utils.data import DataLoader
import torch.optim as optim
from torch.autograd import Variable
drive.mount('/content/gdrive')

#Set CSV column labels
fields = ['file', 'label']

# Get the list of all files and directories, one for malware and for freeware
malware_path = "/content/gdrive/MyDrive/hpml_final_project/dasmalwerk/"
freeware_path = "/content/gdrive/MyDrive/hpml_final_project/portablefreeware/"
malware_dir_list = os.listdir(malware_path)
freeware_dir_list = os.listdir(freeware_path)
malware_files = []
freeware_files = []
for each in malware_dir_list:
    malware_files.append([each, '1'])
for each in freeware_dir_list:
    freeware_files.append([each, '0'])
 
#Write both output lists to CSV
filename = "/content/gdrive/MyDrive/hpml_final_project/input_labels.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(malware_files)
    csvwriter.writerows(freeware_files)
