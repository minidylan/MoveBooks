# This script will move pdf's, Books for me
# from my downloads folder to my Books folder

import os
import shutil
import send2trash

os.chdir('C:/Users/dylan/Downloads')

for filename in os.listdir():
    if filename.endswith('.pdf'):
        shutil.move(filename, 'D:/Books')
