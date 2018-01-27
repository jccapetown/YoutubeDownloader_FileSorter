#When Downloading files fro Youtube, then these files
#will be have the format "Title - Subtitle"
#This script will split files based on the "-", create a folder
#for the first part and move the file into that folder
import sys
import os
import glob
from shutil import move

filetypes = ['*.m4a', '*.mp3']

for filetype in filetypes:
    for filen in glob.glob(filetype):
        print filen
        if "-" in filen:
            index =  filen.index('-')
            foldername = filen[0:index].strip()
            if not os.path.exists(foldername):
                os.makedirs(foldername)
            move(filen, '%s/%s' % (foldername, filen) )
        
