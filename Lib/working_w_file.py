# Reading and writing files
# This is important to gather information and store them into txt file and other formats
# For example: getting video urls in youtube and store them in txt file and then use them in your progra (video downloader)

# To do this,we need to create an file and read it in this file
# To create a file, we need to use the open() function

Open_file =  open("pymodules/Working_files.txt", "r+")

Read_file = Open_file.readline() # This is read the first line of the file
Read_file01 = Open_file.readline() # This is read the second line of the file

print(Read_file)
print(Read_file01)

Open_file.close() # This is important to close the file


Append_file = open("pymodules/Working_files.txt", "a")
Append_file.write("This is the very last line") # This is write a line of text to the file
Append_file.close()


# This will append items inside the list to the file
with open("pymodules/Working_files.txt", "a") as OP:
    Items = ["Alfred", "Bert", "Cindy", "Dennis"]
    for item in Items:
        OP.write(item + "\n")
    OP.close()
    print("Done")


# Opening and Reading text files using Buffer Size
'''
Sometimes, we may want to read a file by buffer size so that our program
does not use too much memory resources. To do that, we can use the
read() function (instead of the readline() function) which allows us
to specify the buffer size we want.
'''

Open_file = open("pymodules/Working_files.txt", "r")
print(Open_file.read(10))


# Opening, Reading and Writing Binary Files
'''
Binary files refer to any file that contains non-text, such as image or video
files. To work with binary files, we simply use the rb or wb mode
'''
# Duplicates images
input_file = open("convert_binary.jpg", 'rb')
output_file = open("convert_binary01.jpg", "wb")


# Deleting and Renaming Files
'''
Two other useful functions we need to learn when working with files are
the remove() and rename() functions. These functions are available in
the os module and have to be imported before we can use them.
'''
import os

os.rename("pymodules/Working_files.txt", "pymodules/Working_files01.txt")
os.remove("pymodules/Working_files01.txt")

# Modes open/write files

    # r: Read
    # w: Write
    # a: Append
    # r+: Read and Write
    # w+: Write and Read
    # a+: Append and Read
    # rb: Read Binary
    # wb: Write Binary
    # ab: Append Binary
    # rb+: Read and Write Binary
    # wb+: Write and Read Binary
    # ab+: Append and Read Binary