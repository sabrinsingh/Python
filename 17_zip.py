#
# Example file for working with filesystem shell methods
#
import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

#remove the already available archive.zip file first.
def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
         
    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    print(root_dir)
    print(tail)
    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("newfile.txt")
      newzip.write("archive.zip")
      
if __name__ == "__main__":
  main()
