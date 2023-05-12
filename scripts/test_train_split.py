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

# Open CSV with all files
filename = "/content/gdrive/MyDrive/hpml_final_project/input_labels.csv"
X = []
y = []

# Create full datasets, both data (X) and labels (y)
with open(filename, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    first = 0
    for row in spamreader:
      if first == 0:
        first = 1
        continue
      X.append(row[0].split(",")[0])
      y.append(row[0].split(",")[1])

#Create Test/Train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

#Write out CSV containing the respective executables and labels for train
train_csv = "/content/gdrive/MyDrive/hpml_final_project/train_labels.csv"
train_out = []
datapath = "/content/gdrive/MyDrive/hpml_final_project/data/"
for i in range(len(y_train)):
  if os.path.isfile(datapath+X_train[i]):
    train_out.append([X_train[i], y_train[i]])
with open(train_csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(train_out)

#Write out CSV containing the respective executables and labels for test
test_csv = "/content/gdrive/MyDrive/hpml_final_project/test_labels.csv"
test_out = []
for i in range(len(y_test)):
  if os.path.isfile(datapath+X_test[i]):
    test_out.append([X_test[i], y_test[i]])
with open(test_csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(test_out)