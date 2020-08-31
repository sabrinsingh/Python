#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  fhand=open('textfile.txt','w+')

  # Open the file for appending text to the end
  fhand = open('textfile.txt','a')

  # write some lines of data to the file
  for i in range(10):
    fhand.write("This is the line " +  str(i) + "\n")
  
  # close the file when done
  fhand.close()
  
  # Open the file back up and read the contents
  fhand = open('textfile.txt','r')
  if fhand.mode == 'r':
    content = fhand.read()
    print(content)
    
if __name__ == "__main__":
  main()
