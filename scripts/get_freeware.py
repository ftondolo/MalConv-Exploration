import argparse
import os
import random
from io import BytesIO
from zipfile import BadZipFile, ZipFile

import requests
from bs4 import BeautifulSoup
import re

import fnmatch

save_dir = "data/"

def get_href(index):
    link = f"http://www.portablefreeware.com/index.php?id={index}"
    html = requests.get(link, allow_redirects=True).text
    soup = BeautifulSoup(html, "html.parser")
    
  
    href = soup.body.find("ul", {"class": "inline app-links group"}).find("li", {"class": "download"}).a["title"]
    
      
    return href
  
def download(index):
    href = get_href(index)
    try:
      source = requests.get(href, allow_redirects=True)
    except:
      return None
    try:
        with ZipFile(BytesIO(source.content)) as f:
            f.extractall(path=save_dir)
    except BadZipFile:
        with open(os.path.join(save_dir, f"{index}.dll"), "w+b") as f:
            f.write(source.content)
    print(f"file {index} ")
def cleanup_dir():

    # get a list of all files in the directory
    all_files = os.listdir(save_dir)

    # loop through all files in the directory
    for file_name in all_files:
        # check if the file does not end with .exe or .dll
        if not fnmatch.fnmatch(file_name, '*.exe') and not fnmatch.fnmatch(file_name, '*.dll'):
            # delete the file
            print(file_name)
            os.remove(os.path.join(save_dir, file_name))

def main():
    indices = [i for i in range(1, 2200)]
    for index in indices:
        
        try:
            download(index)
        except AttributeError:
            continue

    cleanup_dir()


if __name__ == "__main__":
    main()
