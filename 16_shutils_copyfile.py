import os
from os import path
import shutil
import time

src="textfile.txt"
if(path.exists(src)):
    # # modification time of the original file
    # print("Modification time of the original time is ", time.ctime(path.getmtime(src)))
    # copyfile = "bk_" + src 
    # print(copyfile)
    # #creates a file name copyfile and copy the content to the src to it
    # shutil.copy(src, copyfile)
    # print("Modification time of the copy file time is ", time.ctime(path.getmtime(copyfile)))
   
    # #to copymodification time also
    # shutil.copystat(src, copyfile)
    # print("The modification is also copied to the copy file and it is ", time.ctime(path.getmtime(copyfile)))

    # # rename the original file
    # os.rename(copyfile,"newfile.txt")
