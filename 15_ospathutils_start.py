#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time



def main():
  # Print the name of the OS
  #'nt' means that you are running windows, and 'posix' mac.
  print(os.name)

  # Check for item existence and type
  print("The item exits : " + str(path.exists('textfile.txt')))
  print("The item is a file : " + str(path.isfile('textfile.txt')))
  print("The item is a folder : " + str(path.isdir('textfile.txt')))
  
  # Work with file paths
  print("Item path : " + str(path.realpath('textfile.txt')))
  print("Item path and name : " + str(path.split(path.realpath('textfile.txt'))))
  
  # Get the modification time (getmtime)
  t=time.ctime(path.getmtime('textfile.txt'))
  print(t)
  
  # Calculate how long ago the item was modified
  current_time=datetime.datetime.now()
  td= current_time - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")


  
if __name__ == "__main__":
  main()
