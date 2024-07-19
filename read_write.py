#!/usr/bin/python

'''
Below are simple example To write or read or edit files or txt
created by rahul

'''

###### write file #############Start ########

'''open funtion use for read or write file'''

rah_op = open('c://plot//rah_test.txt', 'w') #'w' mode always over write the file
rah_op.write('I can use Python.\n') #\n for new line 
rah_op.close() #This will close all resources from os alloted

rah_op = open('c://plot//rah_test.txt', 'a') #'a' means append mode 
rah_op.write('I can use C shell as well.\n') #\n for new line 
rah_op.close() #This will close all resources from os alloted

###### write file ############# END ########


###### Write file and read file with edits (Line by Line) #############Start ########

'''
Below i created funtion to edit and create new file,
but we can create same without creating funtion to read file
'''

# First, create the file and write to it
rah_jk = open('c://plot//rah_joke.txt', 'a')  # 'a' means append mode
rah_jk.write('Teacher: Why are you late, Rahul?\nRahul: Because of sign.\nTeacher: What sign?\nRahul: The one that says, "School Ahead, Go Slow"\n')
rah_jk.close()

# Now, create a new function to read the file and count words from each line
def read_file():
    with open('c://plot//rah_joke.txt', 'r') as rah_read:  # 'r' for read mode ## The with statement ensures the file is properly closed after reading.
        for line in rah_read:
            word_count = len(line.split())
            rah_jk_count = open('c://plot//rah_joke_count.txt', 'a')
            rah_jk_count.write(f'{line.strip()} -> Word Count: {word_count}\n')

read_file() #Run the funtion to creat updated file

###### Write file and read file with edits (Line by Line) ############# END ########

####################### File open mode ###################### also few other please google it. 
#      'r' --> opens file for reading only. Throws error if file does not exist.
#      'w' --> opens file for writing only. If file doesn't exist then it will create new one. If exist then it will overwrite it. 
#      'r+' --> opens file for both reading and writing.
#      'w+' --> opens file for both reading and writing. If file doesn't exist then it will create new one. If exist then it will overwrite it. 
#      'r' --> opens file in append mode. Whateve you write to file will get appended and orignal content will not be overwrriten. 
