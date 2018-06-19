import sys
print('Enter the file name: ')
file_name = input()

try:
      file = open(file_name,'r')
      file_csv = open(file_name +'.csv','w')
      i=0
      progress = 0.0
      print('\nConverting File! ...')
      
      lines = file.readlines()

      while i<len(lines):
            line = str(lines[i]).split('\t')
            for j in range(0,len(line)):
                  file_csv.write(line[j])
                  if(j!=(len(line)-1)):
                        file_csv.write(',')  
            progress = round(((i+1)*100)/len(lines),2)
            print('Progress.....',progress, end= '\r')
            line = None
            i=i+1

      file.close()
      file_csv.close()
      print('\nCSV conversion done')
      print('\nTotal records = '+ str(len(lines)))
      print('\nTotal number of Columns = '+ str(len(str(lines[0]).split('\t'))))

except IOError:
      print('Could not open the specified file.')
      print('\n Causes:')
      print('\n1. Wrong file name or file name without extension .txt')
      print('\n2. The file is in another directory and the path is not specified.')
finally:
      print('\n\n Thank You for using this software. ')
      print('\nSoftware made by Anupam Anand')
print('\nPress Enter to Exit')
input()
